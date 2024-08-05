from flask import Flask, request, jsonify
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()


@app.route('/api/chatbot', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.generate_response(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
