import random
import datetime
import time

GREETINGS = {
    "responses": [
        "Hello there! How's your day going?",
        "Hi! Nice to see you!",
        "Hey! Ready to chat?",
        "Greetings! What's on your mind today?"
    ],
    "keywords": ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
}

FAREWELLS = {
    "responses": [
        "Goodbye! Hope to chat again soon!",
        "See you later! Take care!",
        "Farewell! Have a wonderful day!",
        "Bye! Don't hesitate to come back if you need anything!"
    ],
    "keywords": ["bye", "goodbye", "see you", "farewell", "exit", "quit"]
}

FEELINGS = {
    "happy": [
        "That's wonderful! What's making you happy today?",
        "Great to hear you're feeling happy!",
        "Happiness is contagious! Thanks for sharing!"
    ],
    "sad": [
        "I'm sorry to hear that. Want to talk about it?",
        "It's okay to feel sad sometimes. I'm here to listen.",
        "Sending virtual hugs your way."
    ],
    "excited": [
        "That's exciting! Tell me more!",
        "Wow! What are you excited about?",
        "Excitement is in the air!"
    ],
    "tired": [
        "Remember to take breaks and rest when needed.",
        "Sometimes a short break can do wonders!",
        "Hope you get some rest soon!"
    ]
}

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't eggs tell jokes? They'd crack each other up!"
]

FACTS = [
    "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat.",
    "Fun fact: Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
    "Interesting: A day on Venus is longer than a year on Venus. It takes Venus 243 Earth days to rotate once, but only 225 Earth days to orbit the Sun.",
    "Cool fact: Bananas are berries, but strawberries aren't.",
    "Amazing: Your nose can remember 50,000 different scents."
]

def get_greeting_response():
    """Returns a random greeting response"""
    return random.choice(GREETINGS["responses"])

def get_farewell_response():
    """Returns a random farewell response"""
    return random.choice(FAREWELLS["responses"])

def get_feeling_response(feeling):
    """Returns a response based on the user's feeling"""
    feeling = feeling.lower()
    for key in FEELINGS:
        if key in feeling:
            return random.choice(FEELINGS[key])
    return "Thanks for sharing how you feel. Want to talk more about it?"

def get_current_time():
    """Returns the current time"""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
    """Returns the current date"""
    now = datetime.datetime.now()
    return now.strftime("%B %d, %Y")

def get_weather_info():
    """Simulates weather information"""
    conditions = ["sunny", "cloudy", "rainy", "windy", "snowy"]
    temperatures = list(range(10, 35))
    return f"It's currently {random.choice(conditions)} with a temperature of {random.choice(temperatures)} degrees Celsius."

def get_advice():
    """Returns random advice"""
    advice_list = [
        "Remember to take breaks when working for long periods.",
        "Drinking water regularly is good for your health!",
        "A good night's sleep can improve your productivity.",
        "Don't forget to appreciate the small things in life.",
        "Learning something new every day keeps your mind sharp."
    ]
    return random.choice(advice_list)

def chatbot_response(user_input):
    """
    This function processes user input and returns a chatbot response
    using enhanced rule-based logic.
    """
    user_input_lower = user_input.lower()

    for keyword in GREETINGS["keywords"]:
        if keyword in user_input_lower:
            return get_greeting_response()

    for keyword in FAREWELLS["keywords"]:
        if keyword in user_input_lower:
            return get_farewell_response()

    if any(phrase in user_input_lower for phrase in ["your name", "who are you", "what are you"]):
        return "I'm ChatBot 1.0, an enhanced rule-based AI chatbot created by Naledi!"

    if any(phrase in user_input_lower for phrase in ["what can you do", "capabilities", "help"]):
        return """I can do several things:
• Have conversations with you
• Tell jokes and fun facts
• Give advice
• Share the current time and date
• Talk about feelings
• Simulate weather information
• And much more! Try asking me anything!"""

    if any(word in user_input_lower for word in ["feel", "feeling", "felt", "mood"]):
        if any(word in user_input_lower for word in ["happy", "good", "great", "awesome"]):
            return get_feeling_response("happy")
        elif any(word in user_input_lower for word in ["sad", "bad", "terrible", "awful"]):
            return get_feeling_response("sad")
        elif any(word in user_input_lower for word in ["excited", "excitement", "thrilled"]):
            return get_feeling_response("excited")
        elif any(word in user_input_lower for word in ["tired", "exhausted", "sleepy"]):
            return get_feeling_response("tired")
        else:
            return "How are you feeling today?"

    if any(word in user_input_lower for word in ["joke", "funny", "make me laugh"]):
        return random.choice(JOKES)

    if any(word in user_input_lower for word in ["fact", "interesting", "did you know", "tell me something"]):
        return random.choice(FACTS)

    if any(word in user_input_lower for word in ["time", "what time", "current time"]):
        return f"The current time is {get_current_time()}."

    if any(word in user_input_lower for word in ["date", "what date", "today's date"]):
        return f"Today's date is {get_current_date()}."

    if any(word in user_input_lower for word in ["weather", "temperature", "forecast"]):
        return get_weather_info()

    if any(word in user_input_lower for word in ["advice", "suggestion", "tip"]):
        return f"Here's some advice: {get_advice()}"

    if any(word in user_input_lower for word in ["thank", "thanks", "appreciate"]):
        return "You're welcome! Is there anything else I can help you with?"

    if any(word in user_input_lower for word in ["how are you", "how do you feel"]):
        return "I'm doing great, thanks for asking! I'm always ready to help. How about you?"

    if any(word in user_input_lower for word in ["who made you", "created you", "your creator"]):
        return "I was created by Siphumelele using Python!"

    if any(word in user_input_lower for word in ["how old are you", "your age"]):
        return "I was just created, so I'm brand new! But I learn from every conversation."

    if any(word in user_input_lower for word in ["favorite", "favourite", "like best"]):
        topics = ["books", "movies", "music", "food", "color"]
        for topic in topics:
            if topic in user_input_lower:
                return f"I don't have personal preferences, but I can tell you that many people enjoy {topic}! What's your favorite {topic}?"

    default_responses = [
        "That's interesting! Tell me more about that.",
        "I see. What are your thoughts on that?",
        "Could you elaborate on that?",
        "Interesting point! Want to explore that topic further?",
        "I understand. Is there anything specific you'd like to know?",
        "Thanks for sharing! I'm learning from our conversation."
    ]
    return random.choice(default_responses)

def run_chatbot():
    """Main function to run the chatbot"""
    print("=" * 50)
    print("ENHANCED AI CHATBOT v1.0")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the conversation")
    print("You can ask about time, date, weather, jokes, facts, advice, and more!")
    print("-" * 50)

    conversation_history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please type something to continue our conversation.")
                continue

            conversation_history.append(f"You: {user_input}")

            response = chatbot_response(user_input)


            conversation_history.append(f"Bot: {response}")

            print("Bot:", end=" ")
            for char in response:
                print(char, end="", flush=True)
                time.sleep(0.02)
            print()

        
            if any(keyword in user_input.lower() for keyword in FAREWELLS["keywords"]):
                print("\n" + "=" * 50)
                print("Conversation Summary:")
                print(f"Total exchanges: {len(conversation_history)//2}")
                print("Thanks for chatting! Here's what we talked about:")
                for i, line in enumerate(conversation_history[-6:], 1):  # Show last 3 exchanges
                    print(f"{i}. {line}")
                print("=" * 50)
                break

        except KeyboardInterrupt:
            print("\n\nBot: Thanks for chatting! Goodbye!")
            break
        except Exception as e:
            print(f"\nBot: Sorry, I encountered an error: {e}")
            print("Let's continue our conversation.")

def main():
    """Main program entry point"""
    print("Initializing Enhanced ChatBot...")
    time.sleep(1)

    while True:
        run_chatbot()

        
        restart = input("\nWould you like to start a new conversation? (yes/no): ").lower().strip()
        if restart not in ['yes', 'y', 'yeah', 'sure']:
            print("\nThank you for using Enhanced AI Chatbot. Have a great day!")
            break
        print("\n" + "=" * 50)
        print("Starting new conversation...")
        print("=" * 50)


if __name__ == "__main__":
    main()

