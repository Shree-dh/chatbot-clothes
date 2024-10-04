from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple list of clothes for demonstration purposes
clothes = {
    "shirts": ["T-shirt", "Dress shirt", "Casual shirt"],
    "pants": ["Jeans", "Chinos", "Shorts"],
    "shoes": ["Sneakers", "Formal shoes", "Boots"]
}

# Simple chatbot function
def chatbot_response(message):
    message = message.lower()
    
    # Greeting responses
    if message in ["hello", "hi", "hey"]:
        return "Hello! How can I assist you today? You can ask about shirts, pants, or shoes."
    
    # Response for clothing inquiry
    if "what type of clothes do you have" in message or "what clothes do you have" in message or "i want to know what type of clothes you have" in message:
        types_of_clothes = ', '.join(clothes.keys())
        return f"We have the following types of clothes: {types_of_clothes}."
    
    if "shirt" in message:
        return f"We have: {', '.join(clothes['shirts'])}."
    elif "pants" in message:
        return f"We have: {', '.join(clothes['pants'])}."
    elif "shoes" in message:
        return f"We have: {', '.join(clothes['shoes'])}."
    else:
        return "I'm sorry, I didn't understand that. Can you ask about shirts, pants, or shoes?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    userText = request.json['message']
    return jsonify(response=chatbot_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
