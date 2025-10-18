# Fruit-Detection-Using-yolov8n

A desktop application for **real-time fruit detection** using **YOLOv8** and a **modern Tkinter GUI**.  
You can detect fruits from your webcam or from uploaded images easily.

---

## 🚀 Features

- 🎥 **Live Webcam Detection** – Detect fruits in real-time.
- 🖼️ **Image Upload Detection** – Analyze static images with the YOLO model.
- 🧩 **User-Friendly GUI** built using Tkinter and ttk themes.
- 🌈 **Color-coded bounding boxes** for each fruit class.
- 🔄 **Refresh and Quit Controls** directly from the app sidebar.

---

## 📂 Project Structure
``` bash
FRUIT_DETECTION/
│
├── models/
│ ├── best.pt # trained YOLOv8 fruit model
│ └── last.pt # optional backup model
│
├── modules/
│ ├── web_cam.py # webcam-based detection logic
│ └── uploader.py # image upload detection logic
│
├── ui/
│ └── app_ui.py # Tkinter-based user interface
│
├── my_outputs/
│ ├── exp1/
│ └── exp12/
│
├── app.py # main launcher
├── requirements.txt # dependencies list
└── README.md # project documentation
```

## ⚙️ Installation

Follow these steps to set up the project on any PC:

### 1. Clone the repository
```bash
https://github.com/Karthik-K-2003/Fruit_Detection_Yolov8.git
```

## 2. Create and activate a virtual environment
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

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```
