from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, File, UploadFile

from app.services.document_service import create_document

router = APIRouter()


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(parents= True, exist_ok=True)

    unique_name = f"{uuid4()_{file.filename}}"
    saved_path = upload_dir / unique_name

    content = await file.read()
    saved_path.write_bytes(content)

    file_size = len(content)
    file_type = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else "unknown"
    storage_path = str(saved_path)

    create_document(
        filename=file.filename,
        file_type=file_type,
        file_size=file_size,
        storage_path=storage_path
    )

    return {"message": "File Uploaded Successfully"}
    