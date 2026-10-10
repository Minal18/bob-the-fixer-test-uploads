"""Sends upload notifications."""
import requests

NOTIFY_URL = "https://hooks.example.com/notify"


def notify_upload_complete(filename: str) -> None:
    requests.post(NOTIFY_URL, json={"event": "upload_complete", "filename": filename}, timeout=5)
