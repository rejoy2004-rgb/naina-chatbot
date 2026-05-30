from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

DOCUMENT_FOLDER = "documents"

all_docs = []

for file in os.listdir(DOCUMENT_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(
            DOCUMENT_FOLDER,
            file
        )

        loader = PyPDFLoader(path)

        docs = loader.load()

        all_docs.extend(docs)

print(f"Loaded {len(all_docs)} pages")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    all_docs
)

print(f"Created {len(chunks)} chunks")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="vector_db"
)

print("Vector DB Created Successfully")