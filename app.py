"""UI placeholder for the motion-estimator project.

This Streamlit app currently provides a minimal interface scaffold only.
It does not run motion-estimation algorithms yet.
"""

from __future__ import annotations

import streamlit as st


def build_ui() -> None:
    """Render the initial Streamlit interface placeholder."""
    st.set_page_config(page_title="Motion Estimator", layout="centered")

    st.title("Video Motion Estimator")
    st.caption("Project scaffold initialized — motion detection is not implemented yet.")

    st.subheader("Planned Workflow")
    st.markdown(
        """
        1. Upload or select a video source.
        2. Configure motion-estimation parameters.
        3. Run processing and review results.
        """
    )

    st.info("Core motion-estimation logic will be added in a future update.")


if __name__ == "__main__":
    build_ui()
