from datetime import datetime
from uuid import uuid4

from app.models.document import Document


def create_document(filename: str, file_type: str, file_size: int, storage_path: str) -> Document:
    return Document(
        document_id=str(uuid4()),
        filename=filename,
        file_type=file_type,
        storage_path=storage_path,
        file_size=file_size,
        upload_time=datetime.utcnow(),
        status="uploaded",
    )