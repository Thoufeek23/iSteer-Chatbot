import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from config import GEMINI_API_KEY, TARGET_URL
from scraper import scrape_website_recursively
from vector_store import chunk_text, create_vector_db
from chatbot import create_chatbot

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

print("Loading and preparing chatbot...")
raw_text = scrape_website_recursively(TARGET_URL)
docs = chunk_text(raw_text)
db = create_vector_db(docs)
chatbot = create_chatbot(db)

app = Flask(__name__, static_folder=STATIC_DIR)
CORS(app)

def clean_response(text):
    remove_phrases = [
        "based on the provided text",
        "from the provided text",
        "according to the provided text",
        "based on the text you provided",
        "provided text suggests",
        "the provided information",
        "Based on the provided text,",
        " , "
    ]
    for phrase in remove_phrases:
        text = text.replace(phrase, "")
    return text.strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Please enter a message."}), 400

    lower_input = user_input.lower()

    contact_keywords = ["contact", "reach out", "get in touch", "speak to someone", "connect me"]
    negative_keywords = ["don't", "do not", "no need", "not", "never"]

    is_contact_intent = any(kw in lower_input for kw in contact_keywords)
    is_negative = any(neg in lower_input for neg in negative_keywords)

    if is_contact_intent and not is_negative:
        return jsonify({
            "response": """
                You can contact iSteer through their official contact page:<br><br>
                <a href="https://www.isteer.com/contact-us" target="_blank" style="text-decoration: none;">
                    <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer;">
                        Visit Here
                    </button>
                </a>
            """
        })

    response = chatbot.run(user_input)
    cleaned_response = clean_response(response)
    return jsonify({"response": cleaned_response})

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)
