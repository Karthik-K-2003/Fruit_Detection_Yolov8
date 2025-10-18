import os
from tkinter import filedialog, Label
from PIL import Image, ImageTk
from ultralytics import YOLO
from modules.web_cam import video_label

# Global variables
upload_label = None

# ✅ Load your fruit classification model
model = YOLO("./models/best.pt")


def upload_image(parent):
    """Allow user to upload an image and run fruit detection."""
    global upload_label

    # Remove webcam feed if open
    if video_label is not None:
        video_label.destroy()

    # Open file picker dialog
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return

    # Run model prediction
    results = model.predict(source=file_path, conf=0.5, verbose=False)
    result = results[0]

    # Draw detections on image
    detected_img = result.plot()

    # Convert to ImageTk format for Tkinter
    img = Image.fromarray(detected_img[..., ::-1])  # BGR → RGB
    img = img.resize((400, 300))
    imgtk = ImageTk.PhotoImage(img)

    # Display image in UI
    if upload_label is None:
        upload_label = Label(parent, image=imgtk, bg="white")
        upload_label.imgtk = imgtk
        upload_label.pack(pady=10)
    else:
        upload_label.configure(image=imgtk)
        upload_label.imgtk = imgtk


def reset_upload():
    """Reset uploaded image display."""
    global upload_label
    if upload_label:
        upload_label.configure(
            image='',
            text="Uploaded Image\n\nClick 'Upload Image' to begin",
            fg="#666666"
        )
        upload_label.imgtk = None
