# 🌊 AI-Based Subsea Pipeline Corrosion Detection and Monitoring System

A Final Year Project (FYP) developed at Universiti Teknologi PETRONAS (UTP) that utilizes deep learning and computer vision techniques to detect corrosion defects on underwater pipelines using BlueROV2 video streams and recorded inspection footage.

---

## 📌 Project Overview

Subsea pipelines are critical assets in offshore oil and gas operations. Traditional pipeline inspections rely heavily on manual visual assessment of underwater footage captured by Remotely Operated Vehicles (ROVs), which can be time-consuming and prone to human error.

This project presents an AI-assisted monitoring system capable of:

- Detecting corrosion defects on underwater pipelines
- Highlighting corrosion regions using bounding boxes
- Supporting near real-time monitoring through BlueROV2 video streams
- Generating inspection reports for maintenance and review
- Saving corrosion evidence frames for later analysis

The system is intended to assist inspection engineers by serving as a decision-support tool rather than replacing human judgment.

---

# 🎯 Objectives

1. Develop an underwater pipeline corrosion dataset.
2. Train and evaluate a deep learning object detection model.
3. Integrate the trained model with BlueROV2 live video streams for real-time or near real-time monitoring.

---

# 🛠 Technologies Used

### Machine Learning

- YOLO (Ultralytics)
- Python

### Computer Vision

- OpenCV

### User Interface

- Streamlit

### Data Processing

- Pandas
- OpenPyXL

### Hardware Platform

- BlueROV2
- Underwater Camera

---

# 📂 Features

## 📁 Video Analysis Mode

Allows users to upload recorded underwater inspection footage.

Features:

- Upload video files
- Automated corrosion detection
- Save detected corrosion frames
- Generate inspection reports (.xlsx)
- Download reports directly from the application

Workflow:

```text
Video Upload
      ↓
YOLO Detection
      ↓
Corrosion Identification
      ↓
Save Defect Frames
      ↓
Generate Inspection Report
```

---

## 📡 Live Monitoring Mode

Connects directly to a BlueROV2 RTSP stream.

Features:

- Live video monitoring
- Corrosion detection overlay
- Visual corrosion alerts
- Near real-time detection

Workflow:

```text
BlueROV2 RTSP Stream
           ↓
      YOLO Model
           ↓
 Detection Overlay
           ↓
 Corrosion Alert
```

---

# 📊 Model Performance

Final YOLO Model Results:

| Metric | Result |
|----------|----------|
| mAP@50 | 95.3% |
| mAP@50-95 | 70.7% |
| Precision | 93.5% |
| Recall | 92.3% |

Inference Performance:

- Approximately 80–100 ms per frame
- Approximately 10–12 FPS
- Near real-time operation

---

# 📷 Dataset Summary

The dataset was collected from two underwater environments:

### Water Tank

- Controlled environment
- Better visibility
- Consistent lighting

### Lake Environment

- Realistic underwater conditions
- Reduced visibility
- Variable lighting
- Increased environmental noise

Dataset Statistics:

- Approximately 4000 images
- Approximately 6500 corrosion annotations
- Approximately 4000 pipe annotations

Class Labels:

- corrosion
- pipe

---

# 📄 Inspection Report Generation

The system automatically generates inspection reports in Excel format.

Example:

```text
Subsea_Pipeline_Inspection_Report_20260702_223145.xlsx
```

Generated report includes:

- Timestamp
- Frame Number
- Detection Type
- Confidence Score
- Saved Image Name

This feature provides an inspection trail that can assist engineers in review and maintenance planning.

---

# 📁 Project Structure

```text
pipeline-defect-monitoring/

│
├── main.py
├── detector.py
├── config.py
│
├── weights/
│   └── best.pt
│
├── saved_frames/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/pipeline-defect-monitoring.git
```

Navigate into the project folder:

```bash
cd pipeline-defect-monitoring
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Launch Streamlit:

```bash
streamlit run main.py
```

The application will open in your web browser:

```text
http://localhost:8501
```

---

# 🚀 Future Improvements

Potential future enhancements include:

- Native BlueOS Docker deployment
- Defect severity assessment
- Multi-defect classification
- Defect tracking
- Cloud deployment
- Database-backed inspection history
- Advanced analytics dashboard

---

# 👩‍💻 Author

**Nur Shaheera Husna Mohd Shahril**  
Bachelor of Computer Science (Hons)  

Final Year Project  
Universiti Teknologi PETRONAS (UTP)

LinkedIn:
https://www.linkedin.com/in/shaheera273

---

# 📜 License

This project is licensed under the MIT License.
