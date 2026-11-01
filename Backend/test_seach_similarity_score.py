from app.vectorstore.chroma_store import get_vector_store

vector_store = get_vector_store()

query = "What is Python?"

results = vector_store.similarity_search_with_score(
    query=query,
    k=5
)

for index, (document, score) in enumerate(results, start=1):
    print(f"\nResult {index}")
    print("Distance:", score)
    print("Content:", document.page_content[:300])
    print("Metadata:", document.metadata)