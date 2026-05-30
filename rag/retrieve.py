from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)
def retrieve_context(query):

    docs = db.similarity_search(
        query,
        k=4
    )
    return "\n\n".join(
        [doc.page_content for doc in docs]
    )