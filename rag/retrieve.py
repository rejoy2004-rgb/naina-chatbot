from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing vector DB
db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

def retrieve_context(query, k=5):
    """
    Retrieve relevant chunks from ChromaDB.
    """

    try:

        docs = db.similarity_search(
            query=query,
            k=k
        )

        if not docs:
            return ""

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        return context

    except Exception as e:

        print(f"Retrieval Error: {e}")

        return ""