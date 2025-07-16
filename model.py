import spacy 
import os 
import json
import pickle
import numpy as np
import tensorflow as tf

# Load spaCy's English model (small version)
nlp = spacy.load("en_core_web_sm")

# Initialize stemmer:
def spacy_stem(word):
    doc = nlp(word)
    return doc[0].lemma_.lower() if len(doc) > 0 else word.lower()

# Opening the File.
with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

# Will have the intents.
intents = data["intents"]

# Text Preprocessing:
for intent in intents:
    for pattern in intent["patterns"]:
        # Tokenize and lemmatize with spaCy
        doc = nlp(pattern)

        # Performing the stemming, by keeping only the stem words and also removes punctuation and spaces
        wrds = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_space]
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent['tag'])

    # Adding all the target labels (e.g., greetings, welcome, etc..):
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

# print("words:\n",words)
# print("Lables:\n", labels)

words = [spacy_stem(w) for w in words if w != "?"]
words = list(set(words))
words.sort()
labels.sort()

# print("\nWords:\n", words)
# print("Labels:\n", labels)

# These will be the Training and Target data, means X and Y
training = []
output = []

out_empty = [0 for _ in range(len(labels))]

# OneHotEncoding
for x, doc in enumerate(docs_x):
    bag = []
    wrds = {spacy_stem(w) for w in doc}
    
    for w in words:
        bag.append(1 if w in wrds else 0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)

# print("\nTraining data:", training)
# print("Output data:", output)

# Training of the Model:
training = np.array(training)
output = np.array(output)

# print("\nTraining data:", training)
# print("Output data:", output)

with open("data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)
    print("Preprocessed data has been saved!!!")

model = tf.keras.Sequential([
    # First input layer.
    tf.keras.layers.Input(shape=(len(training[0]),)),

    # Two hidden layers
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),

    # Output layers
    tf.keras.layers.Dense(len(output[0]), activation='softmax'),
])

# Compiling and Training the mode.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(training, output, epochs=100, verbose=1)


print("\n" + "="*50)
print("TRAINING COMPLETE")
print(f"Final Accuracy: {history.history['accuracy'][-1]:.2%}")
print(f"Final Loss: {history.history['loss'][-1]:.4f}")
print("="*50)

# Saving the Model
try:
    model.save("chatbot_model.keras")
    print("Model successfully saved as 'chatbot_model.keras'")
    print(f"File size: {os.path.getsize('chatbot_model.keras')/1024:.2f} KB")
except Exception as e:
    print(f"Error saving model: {str(e)}")
