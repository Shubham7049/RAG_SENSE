from app.vectorstore.chroma_store import get_vector_store

vector_store = get_vector_store()

print("ChromaDB initialized successfully!")
print("Collection:", vector_store._collection.name)
print("Existing documents:", vector_store._collection.count())