import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)
