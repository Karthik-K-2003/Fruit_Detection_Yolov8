# Waste-Detection-Using-yolov8n

A waste detection system using **YOLOv8** for image and webcam-based classification.

---

## 🚀 Features
- Real-time object detection with webcam
- Image upload and prediction
- YOLOv8 model integration (`best.pt`, `last.pt`)
- Organized outputs for predictions

---

## 📂 Project Structure
``` bash
WD-yolov8n/
│── .venv/ # Virtual environment (ignored in git)
│── assets/ # Static assets (icons, etc.)
│── image-outputs/ # Stores prediction images
│ └── predict/
│── models/ # YOLO model weights
│ ├── best.pt
│ └── last.pt
│── modules/ # Core modules
│ ├── init.py
│ ├── uploader.py # Handles image upload
│ └── web_cam.py # Webcam detection
│── my_outputs/ # Experiment outputs
│ ├── exp1/
│ └── exp12/
│── ui/ # User Interface code
│ ├── init.py
│ └── app_ui.py
│── utils/ # Helper functions
│── main.py # Entry point
│── predict.py # Prediction script
│── requirements.txt # Python dependencies
│── .gitignore
│── README.md
```


---

## ⚙️ Installation

Follow these steps to set up the project on any PC:

### 1. Clone the repository
```bash
https://github.com/manojhp24/Waste-Detection-Using-Yolov8n.git
cd WD-yolov8n
```

## Create and activate a virtual environment
Create Virtual environment
```bash
python -m venv venv
```
Activate in Windows
``` bash
venv\Scripts\activate
```

# Activate (Linux/Mac)
``` bash
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
python main.py
```
