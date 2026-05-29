from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)


def retrieve_context(question):

    docs = db.similarity_search(
        question,
        k=2
    )

    context = ""

    for doc in docs:

        context += doc.page_content
        context += "\n\n"

    return context