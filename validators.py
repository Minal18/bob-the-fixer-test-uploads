"""Input validation helpers."""
from config import get_allowed_extensions


def validate_extension(filename: str) -> bool:
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in get_allowed_extensions()


def validate_size(size_bytes: int, max_mb: int) -> bool:
    return size_bytes <= max_mb * 1024 * 1024
