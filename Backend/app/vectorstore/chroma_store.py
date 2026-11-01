
from langchain_chroma import Chroma
import hashlib
from app.embeddings.embedding_model import get_embedding_model


# Initialize embedding model
embedding_function = get_embedding_model()


def get_vector_store():
    vector_store = Chroma(
        collection_name="rag_sense_documents",
        embedding_function=embedding_function,
        persist_directory="./chroma_db"
    )

    return vector_store
   

#adding chunk to vector store
#if same document is updated than it will use  previous one

def add_documents(vector_store, documents, batch_size=100):

    if not documents:
        print("No documents to add.")
        return

    total = len(documents)

    for start in range(0, total, batch_size):
        batch = documents[start:start + batch_size]

        ids = []

        for index, document in enumerate(batch, start=start):
            source = document.metadata.get("source", "unknown")

            content_hash = hashlib.sha256(
                document.page_content.encode("utf-8")
            ).hexdigest()[:12]

            chunk_id = f"{source}_{content_hash}_{index}"

            chunk_id = hashlib.sha256(
                chunk_id.encode("utf-8")
            ).hexdigest()

            ids.append(chunk_id)

        vector_store.add_documents(
            documents=batch,
            ids=ids
        )

        print(
            f"Processed {min(start + batch_size, total)}/{total} chunks",
            flush=True
        )

    print("All chunks processed successfully!")



def search_documents(vector_store, query, k=5):

    results = vector_store.similarity_search(
        query=query,
        k=k
    )

    return results

