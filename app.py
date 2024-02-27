from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)


def get_response(message):
    # Convert the message to lowercase for case-insensitive matching
    message = message.lower()

    # Define responses for different patterns
    responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "greet_name": ["Nice to meet you, {name}!", "Hello, {name}!", "Hi, {name}!"],
    "weather": ["The weather is sunny today.", "It's raining outside.", "Expect some snow later."],
    "joke": ["Why was the math book sad? Because it had too many problems.", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "Why don't scientists trust atoms? Because they make up everything!"],
    "greet_time": ["Good morning!", "Good afternoon!", "Good evening!"],
    "how_are_you_fine": ["I'm doing fine, thank you.", "I'm feeling great today.", "I'm doing just fine."],
    "how_are_you_not_fine": ["I'm not feeling too well.", "I've been better.", "I'm feeling a bit under the weather."],
    "what_is_your_name": ["I'm just a humble chatbot!", "I'm a bot designed to assist you.", "You can call me ChatBot!"],
    "favorite_food": ["I don't eat, but I've heard good things about pizza!", "I'm more of a fan of data than food.", "I'm a chatbot, so I don't have a favorite food."],
    "hobbies": ["I enjoy chatting with users like you!", "I like helping people with their questions.", "My hobby is learning new things and improving my responses!"],
    "buy_item": ["Are you looking to buy something specific?", "What kind of item are you interested in purchasing?", "Let me know what you're looking for, and I'll see if I can help you find it."],
    "sell_item": ["Are you looking to sell something?", "What item do you have for sale?", "Let me know what you're selling, and I'll try to assist you with finding buyers."]
    }

    # Check if the message matches any predefined patterns
    for pattern, response_list in responses.items():
        if pattern in message:
            return random.choice(response_list)

    # If no matching pattern is found, return a default response
    return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = get_response(user_text)
    return response

if __name__ == "__main__":
    # It's safer to use debug=False in production
    app.run(debug=False)
