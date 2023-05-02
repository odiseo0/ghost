import pickle

import aiofiles
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

from .loaders import PDFLoader


async def ingest():
    """Get documents from web pages."""
    loader = PDFLoader("assets/example.pdf")
    documents = await loader.load_and_split()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    async with aiofiles.open("assets/vectorstore.pkl", "wb") as f:
        serialized = pickle.dumps(vectorstore)
        await f.write(serialized)
