
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunks_documents
from app.vectorstore.chroma_store import get_vector_store, add_documents

# 1. Load document
documents = load_document("data/sample1.pdf")

# 2. Generate chunks
chunks = chunks_documents(documents)

# 3. Initialize ChromaDB
vector_store = get_vector_store()

# 4. Store chunks
add_documents(vector_store, chunks)

# 5. Verify storage
print("Total stored chunks:", vector_store._collection.count())
