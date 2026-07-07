"""
main.py

Pipeline Defect Monitoring System

Contains:

1. Video Analysis Mode
2. Live Monitoring Mode
"""

import os
import cv2
import time
import pandas as pd

from datetime import datetime

import streamlit as st

from detector import detect_frame
from config import (
    RTSP_URL,
    SAVE_FOLDER,
    REPORT_FOLDER
)

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Pipeline Monitor",
    layout="wide"
)

st.title("🌊 Subsea Pipeline Corrosion Monitoring System")

st.caption(
    "Real-time corrosion detection for subsea pipeline inspection using BlueROV2 and YOLO"
)

with st.sidebar:

    st.image("UTP-logo.png", width=120)

    st.title("Pipeline Monitor")

    st.markdown("---")

    st.subheader("🔬 Model")

    st.write("YOLO (Ultralytics)")
    st.sidebar.markdown("---")

    st.sidebar.info(
        """
        **Model Performance**
        
        mAP@50: 95.3%
        
        Precision: 93.5%
        
        Recall: 92.3%
        
        Near Real-Time: ~21 FPS
        """
    )

    st.markdown("---")

    st.title("⚙️ Settings")
    confidence_threshold = st.slider(
    "Confidence Threshold",
        min_value = 0.10,
        max_value = 1.00,
        value = 0.40,
        step = 0.05,
        help = "Higher values reduce false positives but may miss defects."
    )

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.write("Nur Shaheera Husna Mohd Shahril")

    st.write("Universiti Teknologi PETRONAS")

    st.link_button(
        "🔗 LinkedIn Profile",
        "https://www.linkedin.com/in/shaheera273"
    )
    st.link_button(
        "💻 GitHub",
        "https://github.com/sheyhusna/Pipeline-Defect-Monitoring.git"
    )

os.makedirs(SAVE_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)
# --------------------------------------------------
# TABS
# --------------------------------------------------

tab_video, tab_live = st.tabs(
    [
        "📁 Video Analysis",
        "📡 Live Monitoring",
    ]
)

# ==================================================
# VIDEO ANALYSIS TAB
# ==================================================

with tab_video:

    st.header("Upload Video")

    uploaded_file = st.file_uploader(
        "Choose video",
        type=["mp4", "avi", "mov"]
    )

    st.markdown("### Or Use Local File Path")

    video_path = st.text_input(
        "Video Path",
        placeholder=r"C:\Videos\inspection.mp4"
    ).strip().strip('"')

    video_source = None

    if uploaded_file:

        temp_path = "temp_video.mp4"

        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        video_source = temp_path


    elif video_path:

        if not os.path.exists(video_path):

            st.error("Video file not found.")

            video_source = None


        else:

            video_source = video_path

            st.success("Video file found.")

    if video_source:
        if st.button("▶ Process Video"):
            detection_logs = []

            cap = cv2.VideoCapture(video_source)

            frame_count = 0
            corrosion_frames = 0

            progress = st.progress(0)

            total_frames = int(
                cap.get(cv2.CAP_PROP_FRAME_COUNT)
            )

            while cap.isOpened():

                ret, frame = cap.read()

                if not ret:
                    break

                frame_count += 1

                annotated, corrosion, conf = detect_frame(
                    frame,
                    confidence_threshold
                )

                if corrosion:
                    corrosion_frames += 1

                    image_name = f"corrosion_{frame_count}.jpg"

                    filename = f"{SAVE_FOLDER}/{image_name}"

                    cv2.imwrite(
                        filename,
                        annotated
                    )

                    detection_logs.append({
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Frame Number": frame_count,
                        "Detection": "Corrosion",
                        "Confidence": round(conf, 2),
                        "Saved Image": image_name
                    })

                progress.progress(
                    frame_count / total_frames
                )

            cap.release()

            # =========================
            # CREATE EXCEL REPORT
            # =========================

            report_name = None

            if detection_logs:
                report_name = os.path.join(
                    REPORT_FOLDER,
                    datetime.now().strftime(
                        "Subsea_Pipeline_Inspection_Report_%Y%m%d_%H%M%S.xlsx"
                    )
                )

                df = pd.DataFrame(detection_logs)

                df.to_excel(
                    report_name,
                    index=False
                )

            st.success("Processing Complete")

            st.write(
                f"Total Frames: {frame_count}"
            )

            st.write(
                f"Corrosion Frames Saved: {corrosion_frames}"
            )

            if report_name and os.path.exists(report_name):
                with open(report_name, "rb") as file:
                    st.download_button(
                        label="📄 Download Inspection Report",
                        data=file,
                        file_name=report_name,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

    st.subheader("📸 Saved Corrosion Frames")

    saved_files = []

    if os.path.exists(SAVE_FOLDER):

        saved_files = [
            os.path.join(SAVE_FOLDER, f)
            for f in os.listdir(SAVE_FOLDER)
        ]

    cols = st.columns(3)

    for i, img_path in enumerate(saved_files[-9:]):

        with cols[i % 3]:
            st.image(img_path)

# ==================================================
# LIVE MONITORING TAB
# ==================================================

with tab_live:
    st.header("📡 BlueROV2 Live Monitoring")

    st.info(
        """
        The Live Monitoring Module runs as a dedicated
        OpenCV application for lower latency and
        improved real-time performance.
        """
    )

    st.subheader("Launch Command")

    st.code(
        "python live_rov_monitor.py",
        language="bash"
    )

    st.subheader("Live Monitoring Features")

    st.markdown("""
    ✅ RTSP Stream Monitoring

    ✅ YOLO Corrosion Detection

    ✅ Real-Time Bounding Boxes

    ✅ Corrosion Alerts

    ✅ Evidence Frame Capture
    """)

    st.subheader("RTSP Stream")

    st.code(RTSP_URL)

    st.success(
        """
        Recommended Workflow:

        1. Launch BlueOS
        2. Connect BlueROV2
        3. Run:

           python live_rov_monitor.py

        4. Monitor detections in the OpenCV window
        """
    )
