"""Core module for video input and frame display.

This module currently handles reading frames from a webcam or video file and
showing them in a window. Motion detection/estimation is intentionally not
implemented yet.
"""

from __future__ import annotations

from pathlib import Path

import cv2

from utils import is_supported_video_file


WINDOW_NAME = "Motion Estimator - Raw Video"


def resolve_video_source(source: str | Path | int) -> str | int:
    """Resolve a source into a value accepted by ``cv2.VideoCapture``.

    Args:
        source: Webcam index (int), numeric string (e.g., ``"0"``), or file path.

    Returns:
        ``int`` for webcam input or resolved path string for file input.

    Raises:
        FileNotFoundError: If a provided file path does not exist.
        ValueError: If a provided file is not a supported video type.
    """
    # Integers are treated as webcam indices (0 = default webcam).
    if isinstance(source, int):
        return source

    source_text = str(source).strip()

    # Numeric strings are also treated as webcam indices.
    if source_text.isdigit():
        return int(source_text)

    # Otherwise, treat the input as a file path.
    video_path = Path(source_text).expanduser().resolve()
    if not video_path.exists():
        raise FileNotFoundError(f"Video source not found: {video_path}")

    if not is_supported_video_file(video_path):
        raise ValueError(
            f"Unsupported video format '{video_path.suffix}'. "
            "Use one of: .mp4, .avi, .mov, .mkv"
        )

    return str(video_path)


def open_video_capture(source: str | Path | int) -> cv2.VideoCapture:
    """Open a video capture stream from webcam or file."""
    resolved_source = resolve_video_source(source)
    capture = cv2.VideoCapture(resolved_source)

    if not capture.isOpened():
        raise RuntimeError(f"Unable to open video source: {source}")

    return capture


def run_video_display(source: str | Path | int = 0, window_name: str = WINDOW_NAME) -> None:
    """Read frames continuously and display raw video until user exits.

    Press ``q`` in the display window to quit.
    """
    capture = open_video_capture(source)

    try:
        while True:
            # Read one frame at a time from the active source.
            ok, frame = capture.read()
            if not ok:
                # Webcam read errors or end-of-file for videos both stop the loop.
                break

            cv2.imshow(window_name, frame)

            # Wait briefly for keyboard input; quit when the user presses q.
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def estimate_motion_placeholder() -> None:
    """Placeholder for future motion-estimation integration point."""
    raise NotImplementedError(
        "Motion estimation has not been implemented yet. "
        "Use this function as the future integration point."
    )
