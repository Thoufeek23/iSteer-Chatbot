from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def chunk_text(text: str, chunk_size=2000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.create_documents([text])
    return docs

def create_vector_db(docs):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    db = FAISS.from_documents(docs, embeddings)
    return db