import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

DOCUMENT_PATH = "rag/documents"

VECTOR_DB = "rag/vector_db"

documents = []

for file in os.listdir(DOCUMENT_PATH):

    if file.endswith(".pdf"):

        loader = PyPDFLoader(
            os.path.join(DOCUMENT_PATH, file)
        )

        docs = loader.load()

        documents.extend(docs)

print(f"Loaded {len(documents)} pages.")

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200

)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

embeddings = GoogleGenerativeAIEmbeddings(

    model="models/gemini-embedding-001",

    google_api_key=os.getenv("GEMINI_API_KEY")

)

vectorstore = FAISS.from_documents(

    documents=chunks,

    embedding=embeddings

)

vectorstore.save_local(VECTOR_DB)

print("Vector Database Created Successfully.")