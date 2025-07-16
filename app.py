from flask import Flask, request, jsonify, render_template
import chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def startChat():
    data = request.get_json()
    user_query = data.get("message")
    
    
    if not user_query:
        return jsonify({"response": "Please provide a message."}), 400
    
    # print(user_query)

    bot_response = chat.chat(user_query)
    print(bot_response)
    return jsonify({"response": bot_response})


if __name__ == '__main__':
    app.run(debug=True)