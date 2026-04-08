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
* HTML5, CSS3, JavaScript (Vanilla)retriever to the Gemini 1.5 Flash LLM. When a user asks a question via the frontend, the system retrieves the most relevant chunks and uses them as context to generate an accurate answer.
