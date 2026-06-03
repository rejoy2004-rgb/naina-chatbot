import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_community.vectorstores import Chroma
from langchain_huggingface import (
    HuggingFaceEmbeddings
)
DOCUMENT_FOLDER = "documents"

all_docs = []

print("Loading PDFs...")


for file in os.listdir(DOCUMENT_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(
            DOCUMENT_FOLDER,
            file
        )

        print(f"Reading {file}")

        loader = PyPDFLoader(
            pdf_path
        )

        docs = loader.load()

        all_docs.extend(
            docs
        )


print(
    f"Loaded {len(all_docs)} pages"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    all_docs
)

print(
    f"Created {len(chunks)} chunks"
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print(
    "Creating Vector Database..."
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vector_db"
)

db.persist()

print(
    "Vector Database Created Successfully"
)