import tkinter as tk
from tkinter import ttk
from modules.web_cam import open_webcam
from modules.uploader import upload_image


class FruitDetectionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fruit Detection System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f4f6f9")

        self.cap = None
        self.webcam_label = None
        self.upload_label = None

        self.setup_styles()
        self.create_sidebar(self.root)
        self.create_main_layout(self.root)

    def setup_styles(self):
        """Configure custom styles for the application"""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.colors = {
            'primary': '#3498db',
            'secondary': '#2c3e50',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'light': '#ecf0f1',
            'dark': '#34495e',
            'accent': '#9b59b6'
        }

    def create_sidebar(self, parent):
        """Create left sidebar with navigation and stats"""
        sidebar_frame = tk.Frame(parent, bg=self.colors["dark"], width=250)
        sidebar_frame.pack(side='left', fill='y', padx=(0, 5))
        sidebar_frame.pack_propagate(False)

        logo_frame = tk.Frame(sidebar_frame, bg=self.colors['dark'])
        logo_frame.pack(fill='x', pady=20)

        app_title = tk.Label(logo_frame, text="Fruit Detection",
                             font=("Lato", 16, "bold"),
                             bg=self.colors['dark'], fg="white")
        app_title.pack()

        subtitle = tk.Label(logo_frame, text="AI-Powered Detection",
                            font=("Lato", 10),
                            bg=self.colors['dark'], fg="#bdc3c7")
        subtitle.pack()

        nav_frame = tk.Frame(sidebar_frame, bg=self.colors['dark'])
        nav_frame.pack(fill='x', padx=15, pady=20)

        self.create_nav_button(nav_frame, "📷 Open Webcam",
                               lambda: open_webcam(self.webcam_label), self.colors['success'])
        self.create_nav_button(nav_frame, "📤 Upload Image",
                               lambda: upload_image(self.upload_label), self.colors['primary'])
        self.create_nav_button(nav_frame, "❌ Quit",
                               self.root.quit, self.colors['danger'])
        self.create_nav_button(nav_frame, "🔄 Refresh All",
                               self.reset_all, self.colors['warning'])

    @staticmethod
    def create_nav_button(parent, text, command, color):
        btn = tk.Button(parent, text=text, command=command,
                        fg="white", bg=color, relief='flat',
                        cursor='hand2', width=20, pady=8)
        btn.pack(fill='x', pady=5)

    def create_main_layout(self, parent):
        """Enhanced main content layout with title bar + 2 panels (webcam + upload)"""
        self.right_frame = tk.Frame(
            parent, bg=self.colors['light'], padx=5, pady=5)
        self.right_frame.pack(side='left', fill='both', expand=True)

        header_bg_frame = tk.Frame(
            self.right_frame, height=100, bg=self.colors['primary'])
        header_bg_frame.pack(fill='x')
        header_bg_frame.pack_propagate(False)

        title_frame = tk.Frame(header_bg_frame, bg=self.colors['primary'],
                               highlightbackground=self.colors['dark'],
                               highlightthickness=0)
        title_frame.pack(fill='both', expand=True, padx=20, pady=15)

        title_label = tk.Label(title_frame, text="FRUIT DETECTION DASHBOARD",
                               font=("Lato", 20, "bold"),
                               bg=self.colors['primary'],
                               fg="white",
                               )
        title_label.pack(side="left")


        content_container = tk.Frame(self.right_frame, bg=self.colors['light'])
        content_container.pack(fill='both', expand=True, padx=15, pady=15)

        content_frame = tk.Frame(content_container, bg=self.colors['light'],
                                 highlightbackground="#d4d7dd",
                                 highlightthickness=1)
        content_frame.pack(fill='both', expand=True)

        webcam_frame = tk.LabelFrame(content_frame, text="LIVE WEBCAM FEED",
                                     font=("Lato", 12, "bold"),
                                     bg="white", fg=self.colors['dark'],
                                     padx=10, pady=10,
                                     relief="flat", bd=1)
        webcam_frame.pack(side='left', fill='both',
                          expand=True, padx=15, pady=15)

    
        webcam_header = tk.Frame(webcam_frame, bg="white")
        webcam_header.pack(fill='x', pady=(0, 10))

        tk.Label(webcam_header, text="Real-time Detection",
                 font=("Lato", 10),
                 bg="white", fg=self.colors['dark']).pack(side="left")

        controls_frame = tk.Frame(webcam_header, bg="white")
        controls_frame.pack(side="right")

        webcam_display = tk.Frame(webcam_frame, bg="#e0e0e0",
                                  highlightbackground="#cccccc",
                                  highlightthickness=1,
                                  height=400)
        webcam_display.pack(fill='both', expand=True)
        webcam_display.pack_propagate(False)

        self.webcam_label = tk.Label(webcam_display, bg="#e0e0e0",
                                     text="Webcam Feed\n\nClick 'Open Webcam' to start",
                                     font=("Lato", 10), fg="#666666",
                                     compound="center")
        self.webcam_label.pack(fill='both', expand=True, padx=2, pady=2)

        upload_frame = tk.LabelFrame(content_frame, text="IMAGE UPLOAD",
                                     font=("Lato", 12, "bold"),
                                     bg="white", fg=self.colors['dark'],
                                     padx=10, pady=10,
                                     relief="flat", bd=1)
        upload_frame.pack(side='left', fill='both',
                          expand=True, padx=15, pady=15)

        upload_header = tk.Frame(upload_frame, bg="white")
        upload_header.pack(fill='x', pady=(0, 10))

        tk.Label(upload_header, text="Static Image Analysis",
                 font=("Lato", 10),
                 bg="white", fg=self.colors['dark']).pack(side="left")

        upload_display = tk.Frame(upload_frame, bg="#e0e0e0",
                                  highlightbackground="#cccccc",
                                  highlightthickness=1,
                                  height=400)
        upload_display.pack(fill='both', expand=True)
        upload_display.pack_propagate(False)

        self.upload_label = tk.Label(upload_display, bg="#e0e0e0",
                                     text="Uploaded Image\n\nClick 'Upload Image' to begin",
                                     font=("Lato", 10), fg="#666666",
                                     compound="center")
        self.upload_label.pack(fill='both', expand=True, padx=2, pady=2)

    @staticmethod
    def reset_all():
        """Reset both webcam and upload sections"""
        from modules.web_cam import stop_webcam
        from modules.uploader import reset_upload

        stop_webcam()

        reset_upload()

    def run(self):
        self.root.mainloop()