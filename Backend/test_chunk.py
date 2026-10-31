from app.ingestion.loader import load_document
from app.ingestion.chunker import chunks_documents

documents = load_document("data/sample.pdf")

print("Original documents:", len(documents))

chunks = chunks_documents(documents)

print("Total chunks generated:", len(chunks))

for index, chunk in enumerate(chunks):

    print(f"\n--- Chunk {index + 1} ---")

    print("Metadata:", chunk.metadata)
    print("Content:", chunk.page_content[:200])
    print("Character count:", len(chunk.page_content))