import pickle
import spacy
import random
import json
import tensorflow as tf
import numpy as np

nlp = spacy.load("en_core_web_sm")
model = tf.keras.models.load_model("chatbot_model.keras")

with open("data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f) 

with open("intents.json") as file:
    data = json.load(file)

def spacy_stem(word):
    doc = nlp(word)
    return doc[0].lemma_.lower() if len(doc) > 0 else word.lower()

def bag_of_words(s, words):
    bag = np.zeros(len(words), dtype=np.float32)

    doc = nlp(s)
    s_words = {token.lemma_.lower() for token in doc 
              if not token.is_punct and not token.is_space}

    for i, word in enumerate(words):
        if word in s_words:
            bag[i] = 1.0

    return bag

def chat(query: str) -> str:
    intents = data["intents"]
        
    bag = bag_of_words(query, words)
    bag = np.array([bag])

    # Make prediction
    result = model.predict(bag)
    result_index = np.argmax(result)
    tag = labels[result_index]

    for intent in intents:
        if tag == intent['tag']:
            responses = intent['responses']
    response = random.choice(responses)

    return response