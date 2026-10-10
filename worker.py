"""Glue code tying upload handling together."""
from notifications import notify_upload_complete
from scheduler import should_run_cleanup
from uploader import delete_upload, save_upload


def handle_upload_request(payload: dict) -> dict:
    result = save_upload(payload["filename"], payload["size_bytes"], payload["content"])
    if result["status"] == "ok":
        notify_upload_complete(payload["filename"])
    return result


def handle_delete_request(payload: dict) -> dict:
    return delete_upload(payload["filename"])


def handle_tick() -> None:
    if should_run_cleanup():
        pass  # cleanup logic placeholder
