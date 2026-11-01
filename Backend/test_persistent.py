from app.vectorstore.chroma_store import get_vector_store

vector_store = get_vector_store()

print("ChromaDB reopened successfully!")
print("Total stored chunks:", vector_store._collection.count())