# Motion Estimator

Motion Estimator is a Python project scaffold for future **video motion estimation** development.

> ✅ Current status: project structure and dependencies are initialized.
> 
> 🚧 Motion-estimation logic is intentionally **not implemented yet**.

## Project Overview

This repository is set up to support a clean progression from scaffolding to implementation:

- **`motion.py`**: Core module for video source handling and frame-display loop (motion logic pending).
- **`run_video.py`**: CLI runner that opens webcam/video and displays raw frames.
- **`app.py`**: Streamlit UI placeholder for future interactive workflows.
- **`utils.py`**: Shared helper functions and utility constants.
- **`requirements.txt`**: Runtime dependencies for computer vision and UI development.

## Requirements

- Python 3.10+
- pip

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd motion-estimator
   ```

2. **Create and activate a virtual environment**

   macOS/Linux:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the raw video runner**
   ```bash
   # Default webcam
   python run_video.py --webcam 0

   # Video file
   python run_video.py --video ./path/to/video.mp4
   ```

   Press `q` in the video window to quit.

5. **Run the UI placeholder**
   ```bash
   streamlit run app.py
   ```

## Next Steps

- Implement the motion-estimation pipeline in `motion.py`.
- Add frame-processing utilities and validation helpers in `utils.py`.
- Expand Streamlit controls and result visualizations in `app.py`.
- Add unit tests and code-quality tooling.
