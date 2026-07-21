import os

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

from langchain_community.vectorstores import FAISS

from rag.prompts import RAG_PROMPT

VECTOR_DB = "rag/vector_db"


def ask_rag(question):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectorstore = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    answer = response.content

    sources = []

    for doc in docs:
        source = doc.metadata.get("source")
        page = doc.metadata.get("page")

        if source:
            sources.append(
                f"{os.path.basename(source)} (Page {page + 1})"
            )

    return {
        "answer": answer,
        "sources": list(set(sources))
    }