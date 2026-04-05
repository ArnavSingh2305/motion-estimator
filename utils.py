"""Shared helper utilities for the motion-estimator project.

All helpers in this module are lightweight scaffolding utilities.
"""

from __future__ import annotations

from pathlib import Path


SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv"}


def is_supported_video_file(file_path: str | Path) -> bool:
    """Return ``True`` when a path has a supported video-file extension.

    Args:
        file_path: Candidate file path supplied by a user or caller.

    Returns:
        ``True`` if the file extension is currently listed as supported,
        otherwise ``False``.
    """
    suffix = Path(file_path).suffix.lower()
    return suffix in SUPPORTED_VIDEO_EXTENSIONS


def format_status_message(message: str) -> str:
    """Format a simple status message for logging or UI display."""
    return f"[motion-estimator] {message.strip()}"
