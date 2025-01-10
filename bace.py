from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    # Example response logic (replace with AI logic later)
    ai_response = f"AI response to: {user_message}"
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
