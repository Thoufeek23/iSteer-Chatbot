from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def create_chatbot(vector_db):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    retriever = vector_db.as_retriever()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
