
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunks_documents
from app.embeddings.embedding_model import get_embedding_model

# 1. Load document
documents = load_document("data/sample.pdf")
print("Documents loaded:", len(documents))

# 2. Chunk documents
chunks = chunks_documents(documents)
print("Chunks generated:", len(chunks))

# 3. Generate embeddings
embedding_model = get_embedding_model()
vectors = embedding_model.embed_documents(
    [chunk.page_content for chunk in chunks]
)

print("Embeddings generated:", len(vectors))
print("Vector dimensions:", len(vectors[0]))

# 4. Verify metadata
print("Sample metadata:", chunks[0].metadata)

print("\nDay 1 pipeline test completed!")
