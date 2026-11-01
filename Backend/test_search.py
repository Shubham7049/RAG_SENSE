
from app.vectorstore.chroma_store import (
    get_vector_store,
    search_documents
)

# Initialize ChromaDB
vector_store = get_vector_store()

# Ask a question
query = "What is Python used for?"

# Retrieve top 5 relevant chunks
results = search_documents(
    vector_store,
    query,
    k=5
)

# Display results
print("\nRetrieved Documents:\n")

for index, result in enumerate(results, start=1):
    print(f"\nResult {index}")
    print("Content:", result.page_content)
    print("Metadata:", result.metadata)
