from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os


def extract_key_points_from_response(query):
    chat_model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
You are an expert text analyst and researcher. Please extract the top 5 key points from the given context.
Here is the context: {query}:
"""
    llm_response = chat_model.predict(prompt)
    key_points = llm_response.strip().split("\n")
    key_points = [f". ••{sentence.strip()}" for i, sentence in enumerate(key_points) if sentence.strip()]
    return key_points