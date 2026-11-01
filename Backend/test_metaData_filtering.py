from app.vectorstore.chroma_store import get_vector_store

vector_store = get_vector_store()

query = "What is an embedding?"

results = vector_store.similarity_search(
    query=query,
    k=5,
    filter={"source": "data\\sample1.pdf"}
)

print("Total results:", len(results))

for index, doc in enumerate(results, start=1):
    print(f"\nResult {index}")
    print("Content:", doc.page_content[:300])
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))