# app/repositories/in_memory_repository.py
from app.models.document import Document
from app.repositories.base_repository import BaseDocumentRepository

class InMemoryDocumentRepository(BaseDocumentRepository):
    def __init__(self):
        self._documents: dict[str, Document] = {}

    def add(self, document: Document) -> None:
        self._documents[document.document_id] = document

    def get(self, document_id: str) -> Document | None:
        return self._documents.get(document_id)