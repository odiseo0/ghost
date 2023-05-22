import aiofiles
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from pypdf import PdfReader


class PDFLoader(BaseLoader):
    """Custom PDF loader."""

    async def load(self) -> list[Document]:
        async with aiofiles.open(self.file_path, "rb") as f:
            reader = PdfReader(f)

            return [
                Document(
                    page_content=page.extract_text(),
                    metadata={"source": self.file_path, "page": i},
                )
                for i, page in enumerate(reader.pages)
            ]

    async def load_and_split(
        self, text_splitter: TextSplitter | None = None
    ) -> list[Document]:
        """Load documents and split into chunks."""
        if text_splitter is None:
            _text_splitter: TextSplitter = RecursiveCharacterTextSplitter()
        else:
            _text_splitter = text_splitter

        docs = await self.load()

        return _text_splitter.split_documents(docs)
