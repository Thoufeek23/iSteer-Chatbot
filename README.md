# iSteer Chatbot

An intelligent, full-stack web application featuring a Retrieval-Augmented Generation (RAG) chatbot. The iSteer Chatbot dynamically crawls a target website, processes and indexes its content, and uses Google's Gemini AI to answer user queries with high accuracy based on the scraped context.

## 🚀 Features

* **Dynamic Web Scraping:** Automatically crawls and extracts text from up to 100 internal pages of a specified target URL.
* **Retrieval-Augmented Generation (RAG):** Chunks scraped text and converts it into embeddings using `GoogleGenerativeAIEmbeddings`, storing them in a local FAISS vector database for rapid semantic search.
* **Powered by Gemini AI:** Utilizes the `gemini-1.5-flash` model via LangChain to generate contextual, accurate, and conversational responses.
* **Custom Intent Handling:** Intercepts specific user intents (like "contact" or "reach out") to serve custom HTML responses with direct links to the company's contact page.
* **Modern UI/UX:** A clean, responsive frontend built with vanilla HTML/CSS/JS, featuring typing indicators, auto-scrolling, and a polished chat interface.

## 🛠️ Tech Stack

**Backend:**
* [Python 3.8+](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/) & [Flask-CORS](https://flask-cors.readthedocs.io/)
* [LangChain](https://www.langchain.com/) & [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai)
* [FAISS](https://github.com/facebookresearch/faiss) (Vector Store)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) & [html2text](https://github.com/Alir3z4/html2text) (Scraping)

**Frontend:**
* HTML5, CSS3, JavaScript (Vanilla)

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
* Python 3.8 or higher
* pip (Python package installer)
* A valid [Google Gemini API Key](https://aistudio.google.com/)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/iSteer-Chatbot.git](https://github.com/yourusername/iSteer-Chatbot.git)
   cd iSteer-Chatbot
Set up a virtual environment (Recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the dependencies:
Note: Ensure Flask, Flask-CORS, and python-dotenv are installed alongside the requirements.

Bash
pip install -r backend/requirements.txt
pip install flask flask-cors python-dotenv
Configure Environment Variables:
Create a .env file in the backend/ directory and add your Gemini API key and the target URL:

Code snippet
GEMINI_API_KEY=your_google_gemini_api_key_here
TARGET_URL=[https://www.isteer.com/](https://www.isteer.com/)
🚀 Running the Application
Start the Flask server from the root directory:

Bash
python backend/main.py
Note: On startup, the application will scrape the TARGET_URL, generate embeddings, and build the FAISS vector database. This may take a moment depending on the size of the website.

Open your web browser and navigate to:

Plaintext
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
📂 Project Structure
Plaintext
iSteer-Chatbot/
├── backend/
│   ├── chatbot.py        # LangChain RetrievalQA setup
│   ├── config.py         # Environment variable configuration
│   ├── main.py           # Flask application and API routes
│   ├── scraper.py        # BeautifulSoup web scraping logic
│   ├── vector_store.py   # Text splitting and FAISS DB creation
│   ├── requirements.txt  # Python dependencies
│   └── .env              # Environment variables (not in version control)
└── static/
    ├── index.html        # Chatbot UI
    ├── script.js         # Frontend logic and API integration
    ├── style.css         # UI styling
    └── isteer-logo.png   # Header logo
🧠 How It Works
Initialization (main.py): The app starts by invoking the scraper.

Scraping (scraper.py): It fetches the TARGET_URL, maps internal links, and converts the HTML payload into clean Markdown text.

Embedding (vector_store.py): The Markdown text is split into chunks (2000 characters with 200 overlap). These chunks are embedded using Google's embedding model and stored in a FAISS index.

Chat Interface (chatbot.py): LangChain connects the FAISS retriever to the Gemini 1.5 Flash LLM. When a user asks a question via the frontend, the system retrieves the most relevant chunks and uses them as context to generate an accurate answer.
