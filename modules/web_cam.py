import cv2
from tkinter import messagebox, Label
from PIL import Image, ImageTk
from ultralytics import YOLO

# Webcam & display configuration
WEBCAM_ID = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CONFIDENCE_THRESHOLD = 0.5
UPDATE_INTERVAL = 10
FONT_SCALE = 0.6
FONT_THICKNESS = 2
TEXT_BG_PADDING = 4

CLASS_COLORS = {
    0: (255, 0, 0),
    1: (0, 255, 0),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (255, 0, 255),
    5: (0, 165, 255),
    6: (128, 128, 128),
}

DEFAULT_COLOR = (0, 255, 0)

cap = None
video_label = None
upload_label = None
is_webcam_running = False

model = YOLO("./models/best.pt")


def open_webcam(parent):
    """Open webcam and start fruit detection"""
    global cap, video_label, upload_label, is_webcam_running

    if upload_label is not None:
        upload_label.destroy()
        upload_label = None

    if is_webcam_running:
        stop_webcam()
        return

    cap = cv2.VideoCapture(WEBCAM_ID)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    if video_label is None or not video_label.winfo_exists():
        video_label = Label(parent, bg="black",
                            text="Starting webcam...\n\nClick 'Open Webcam' again to stop",
                            fg="white", font=("Arial", 10), compound="center")
        video_label.pack(pady=10)

    is_webcam_running = True
    update_frame(parent)


def update_frame(parent):
    """Update webcam frame with fruit detection"""
    global cap, video_label, is_webcam_running

    if not is_webcam_running or video_label is None or not video_label.winfo_exists():
        return

    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Error", "Failed to capture frame from webcam")
        stop_webcam()
        return

    frame_resized = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
    results = model.predict(frame_resized, verbose=False,
                            conf=CONFIDENCE_THRESHOLD)[0]

    if results.boxes is not None:
        for box, conf, cls in zip(results.boxes.xyxy, results.boxes.conf, results.boxes.cls):
            x1, y1, x2, y2 = map(int, box)
            class_id = int(cls)
            confidence = float(conf)

            color = CLASS_COLORS.get(class_id, DEFAULT_COLOR)
            class_name = results.names[class_id]
            label = f"{class_name} {confidence:.2f}"

            cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)
            (text_width, text_height), _ = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, FONT_THICKNESS
            )
            text_y = max(y1 - 10, text_height + 5)
            cv2.rectangle(frame_resized,
                          (x1, text_y - text_height - TEXT_BG_PADDING),
                          (x1 + text_width + TEXT_BG_PADDING,
                           text_y + TEXT_BG_PADDING),
                          color, -1)
            cv2.putText(frame_resized, label, (x1, text_y),
                        cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, (255, 255, 255), FONT_THICKNESS)

    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    imgtk = ImageTk.PhotoImage(Image.fromarray(frame_rgb))

    if video_label is not None and video_label.winfo_exists():
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk, text="")
    else:
        video_label = Label(parent, image=imgtk, bg="black")
        video_label.imgtk = imgtk
        video_label.pack(pady=10)

    if is_webcam_running:
        video_label.after(UPDATE_INTERVAL, lambda: update_frame(parent))


def stop_webcam():
    """Stop webcam feed and cleanup"""
    global cap, video_label, is_webcam_running

    is_webcam_running = False

    if cap:
        cap.release()
        cap = None

    if video_label and video_label.winfo_exists():
        video_label.configure(
            image='',
            text="Webcam stopped\n\nClick 'Open Webcam' to start again",
            fg="white",
            font=("Arial", 10)
        )
