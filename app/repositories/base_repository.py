# app/repositories/base_repository.py
from abc import ABC, abstractmethod
from app.models.document import Document

class BaseDocumentRepository(ABC):
    @abstractmethod
    def add(self, document: Document) -> None:
        pass

    @abstractmethod
    def get(self, document_id: str) -> Document | None:
        pass