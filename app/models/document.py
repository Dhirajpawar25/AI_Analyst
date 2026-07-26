from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Document(BaseModel):
    document_id: Optional[str] = None
    filename: str
    file_type: str
    storage_path: str
    upload_time: datetime = Field(default_factory=datetime.utcnow)
    file_size: int
    status: str = "uploaded"
    row_count: Optional[int] = None
    column_count: Optional[int] = None
    column_names: list[str] = Field(default_factory=list)
