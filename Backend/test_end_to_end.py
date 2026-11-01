from app.ingestion.loader import load_document
from app.ingestion.chunker import chunks_documents
from app.vectorstore.chroma_store import (
    get_vector_store,
    add_documents,
    search_documents
)

# 1. Load PDF
file_path = "data/sample.pdf"

documents = load_document(file_path)
print("1. Documents loaded:", len(documents))

# 2. Chunk documents
chunks = chunks_documents(documents)
print("2. Chunks generated:", len(chunks))

# 3. Initialize ChromaDB
vector_store = get_vector_store()
print("3. ChromaDB initialized")

# 4. Insert chunks
add_documents(vector_store, chunks)
print("4. Documents inserted")

# 5. Check collection count
print("5. Total stored chunks:",
      vector_store._collection.count())

# 6. Perform similarity search
query = "What is an embedding?"

results = search_documents(
    vector_store,
    query,
    k=5
)

print("\n6. Retrieved Results:")

for index, doc in enumerate(results, start=1):
    print(f"\nResult {index}")
    print("Content:", doc.page_content[:300])
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))