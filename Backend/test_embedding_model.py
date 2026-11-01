
from app.embeddings.embedding_model import get_embedding_model

embeddings = get_embedding_model()

texts = [
    "Python is a programming language.",
    "Machine learning uses algorithms to learn from data.",
    "पायथन एक प्रोग्रामिंग भाषा है।"
]

vectors = embeddings.embed_documents(texts)

print("Embedding generation successful!")
print("Number of embeddings:", len(vectors))
print("Vector dimensions:", len(vectors[0]))

query_vector = embeddings.embed_query("What is Python?")

print("Query vector dimensions:", len(query_vector))
