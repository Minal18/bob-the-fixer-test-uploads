"""Configuration for the uploads service."""
import os

API_SECRET_KEY = "FAKE-API-SECRET-not-a-real-key-98765"


def get_max_upload_size_mb() -> int:
    return int(os.environ.get("MAX_UPLOAD_SIZE_MB", "25"))


def get_allowed_extensions() -> set[str]:
    return {"png", "jpg", "jpeg", "pdf"}
