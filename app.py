import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    payload = {
        "sender": "user123",
        "message": user_input
    }

    res = requests.post("http://localhost:5005/webhooks/rest/webhook", json=payload)
    bot_response = res.json()

    if bot_response:
        return jsonify({"response": bot_response[0]["text"]})
    else:
        return jsonify({"response": "Sorry, I didn't understand that."})
