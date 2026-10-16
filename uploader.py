"""Handles file upload storage."""
import os

from config import get_max_upload_size_mb
from validators import validate_extension, validate_size

UPLOAD_DIR = "/var/uploads"


def save_upload(filename: str, size_bytes: int, content: bytes) -> dict:
    if not validate_extension(filename):
        return {"status": "error", "message": "invalid extension"}
    if not validate_size(size_bytes, get_max_upload_size_mb()):
        return {"status": "error", "message": "file too large"}

    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(content)
    return {"status": "ok", "path": path}


def delete_upload(filename: str) -> dict:
    path = os.path.join(UPLOAD_DIR, filename)
    os.remove(path)
    return {"status": "ok"}
