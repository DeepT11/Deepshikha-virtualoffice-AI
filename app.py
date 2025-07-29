#  This code contains backend logic for a virtual office AI application.

from flask import Flask, request, jsonify, render_template
from nlp_utils import classify_intent
from api_hooks import handle_intent

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    user_id = request.json.get("user_id", "123")  # Simulated fallback
    tag = classify_intent(user_input)
    response = handle_intent(tag, user_input, user_id)
    return jsonify({"response": response})



if __name__ == '__main__':
    app.run(debug=True, port=5005)

