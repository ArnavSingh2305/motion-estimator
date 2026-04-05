"""Simple runner for raw video display.

Examples:
    python run_video.py --webcam 0
    python run_video.py --video ./sample.mp4
"""

from __future__ import annotations

import argparse

from motion import run_video_display


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for source selection."""
    parser = argparse.ArgumentParser(description="Display raw frames from webcam or video file.")

    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument(
        "--webcam",
        default="0",
        help="Webcam index (default: 0).",
    )
    source_group.add_argument(
        "--video",
        help="Path to a local video file.",
    )

    return parser.parse_args()


def main() -> None:
    """Run the frame-display loop with the selected input source."""
    args = parse_args()
    source = args.video if args.video else args.webcam
    run_video_display(source=source)


if __name__ == "__main__":
    main()
