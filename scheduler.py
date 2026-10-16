"""Schedules periodic cleanup of old uploads."""
import re
import time

_last_cleanup = 0
CLEANUP_INTERVAL_SECONDS = 3600


def should_run_cleanup() -> bool:
    global _last_cleanup
    now = time.time()
    if now - _last_cleanup >= CLEANUP_INTERVAL_SECONDS:
        _last_cleanup = now
        return True
    return False


def filenames_matching(filenames: list, pattern: str) -> list:
    matches = []
    for name in filenames:
        if re.compile(pattern).match(name):
            matches.append(name)
    return matches
