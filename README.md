# FAQs Chatbot

A smart chatbot that can understand travel-related questions and give quick and helpful answers. It uses machine learning and language processing to talk like a human and respond correctly.
 

## 🖥️ User Interface Overview

The FAQs Chatbot's user interface is designed to be simple, responsive, and interactive, making it easy for users to ask questions and receive answers in real-time.


![imag](https://github.com/user-attachments/assets/514646f5-ad08-4606-9b67-90946a283d38)


Key Elements:
- **Chat Window:** A central area where users can type their queries and view responses from the bot.
- **Input Box:** Allows users to enter their travel-related questions.
- **Send Button:** Triggers the chatbot to process the query and display an answer.
- **Bot Response Area:** Dynamically updates to show the chatbot's replies in a conversational format.
- **Responsive Design:** Fully optimized for desktop, tablet, and mobile devices using HTML/CSS.


## 🎬 Project Demonstration

![image](https://github.com/user-attachments/assets/51002973-e8ee-47ad-8bdf-45438d50a339)

### Interaction Flow:

- User types a question in the input field.
- The query is sent to the Flask backend.
- The model predicts the intent using TensorFlow and NLP (SpaCy).
- A relevant answer is selected and displayed in the chat window.


## 🧩 Architectural Design

<img width="1509" height="700" alt="image" src="https://github.com/user-attachments/assets/944b354d-a411-4742-ac0e-c09fd4e9ee52" />

The chatbot is built using **Flask** as the backend, **HTML/CSS/JS** for the user interface, and tools like **TensorFlow** and **SpaCy** for intent recognition and prediction. A custom intents.json file stores predefined categories and responses.


## 🧰 Tech Stack

| Layer            | Technologies Used                                          |
|------------------|------------------------------------------------------------|
| **Frontend**     | HTML, CSS, JavaScript                                      |
| **Backend**      | Flask (Python Web Framework)                               |
| **NLP**          | SpaCy (for text preprocessing and tokenization)            |
| **Machine Learning** | TensorFlow (for training and intent classification)     |
| **Data Handling**| Custom `intents.json` file (predefined Q&A dataset)        |
| **Model Format** | `.keras` file (Keras-trained TensorFlow model)                |


## 🔄 How It Works

1. **User Input**  
   The user sends a query via the chatbot interface in the browser.

2. **Frontend to Backend**  
   The input is sent to the Flask backend using JavaScript (typically via a POST request).

3. **Preprocessing & Prediction**  
   The backend uses SpaCy to preprocess the text and passes it to the trained TensorFlow model.

4. **Intent Classification**  
   The model predicts the intent of the user’s query (e.g., flight info, visa, currency).

5. **Response Retrieval**  
   Based on the predicted intent, a matching response is fetched from the `intents.json` file.

6. **Reply to User**  
   The response is sent back to the frontend and displayed in the chat window.

> ⚙️ Behind the scenes, the system uses a simple **rule-based + ML hybrid architecture** to deliver fast and accurate answers to travel-related FAQs.


## ✨ Features

- 🤖 **AI-Powered Chatbot**  
  Understands and responds to travel-related questions using a trained machine learning model.

- 🧠 **Intent Recognition**  
  Classifies user queries into predefined categories using NLP and TensorFlow.

- 📚 **Custom Intent Dataset**  
  Uses a handcrafted `intents.json` file containing common travel questions and answers.

- 💬 **Real-Time Interaction**  
  Instant responses via a seamless chat interface built with HTML, CSS, and JavaScript.

- 🛠️ **Lightweight Flask Backend**  
  Fast and easy-to-deploy Python server to handle logic and model inference.

- 🗣️ **Natural Language Processing**  
  Text preprocessing powered by SpaCy for more accurate intent classification.

- 📱 **Responsive UI**  
  Chat interface works smoothly across desktop, tablet, and mobile devices.

- 🧩 **Modular Architecture**  
  Cleanly separated UI, backend, and model logic for easy customization and scaling.


## ⚙️ Setup Instructions

### 🛠️ Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (to clone the repository)


### 📦 Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/travel-faqs-chatbot.git
   cd travel-faqs-chatbot
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

### 🚀 Running the Project

1. **Start the Flask Server**
   ```bash
   python app.py
   ```

2. **Access the Chatbot**
   Open your browser and go to: [localhost:5000](http://127.0.0.1:5000)


## 🗂️ Project Structure

```bash
currency-converter-chatbot/
│
├── .gitignore                   # Git ignore rules (should include .venv, .env, __pycache__)
├── app.py                       # Main Flask application handling webhook logic
├── chat.py                      # Chatbot logic and ML integration
├── chatbot_model.keras          # Trained TensorFlow model 
├── data.pickle                  # Contains the preprocessed data (words, labels)
├── intents.json                 # This file has the intents for the Chatbot
├── model.py                     # Model training file
├── requirements.txt             # List of Python dependencies
└── README.md                    # Project documentation
```


## 🙏 Acknowledgements

I would like to thank the following tools, libraries, and communities for making this project possible:

- [TensorFlow](https://www.tensorflow.org/) – for building and training the intent classification model
- [SpaCy](https://spacy.io/) – for natural language preprocessing
- [Flask](https://flask.palletsprojects.com/) – for creating a lightweight and scalable backend
- [NLTK](https://www.nltk.org/) – for supporting text cleaning and processing
- [JavaScript, HTML, CSS] – for designing a responsive and interactive user interface

> The open-source community – for continuous support, resources, and inspiration

## 🙌 Thank You
Thank you for taking the time to explore this project!
I hope this spam detection system is helpful for learning, experimentation, and real-world understanding of text classification.

If you have any feedback, suggestions, or improvements, feel free to reach out or raise an issue.
Happy coding! 🚀

