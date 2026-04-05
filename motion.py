"""Core module for video motion estimation.

This file intentionally contains only project scaffolding.
Motion-estimation algorithms will be added in a later iteration.
"""

from __future__ import annotations

from pathlib import Path


def load_video_source(source: str | Path) -> Path:
    """Normalize and validate a video source path.

    Args:
        source: Path to a local video file.

    Returns:
        A resolved ``Path`` object.

    Raises:
        FileNotFoundError: If the provided source path does not exist.

    Note:
        This helper prepares input handling only. No video processing is
        performed yet.
    """
    video_path = Path(source).expanduser().resolve()
    if not video_path.exists():
        raise FileNotFoundError(f"Video source not found: {video_path}")
    return video_path


def estimate_motion_placeholder() -> None:
    """Placeholder entry point for future motion-estimation logic.

    This function is intentionally unimplemented to keep the project focused on
    structure setup at this stage.
    """
    raise NotImplementedError(
        "Motion estimation has not been implemented yet. "
        "Use this function as the future integration point."
    )
