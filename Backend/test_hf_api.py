
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="deepinfra",
    api_key=os.getenv("HF_TOKEN")
)

vector = client.feature_extraction(
    "Python is used in machine learning.",
    model="Qwen/Qwen3-Embedding-0.6B"
)

print("API connection successful!")
print("Vector dimensions:", vector.shape)
print("First five values:", vector.flatten()[:5])
