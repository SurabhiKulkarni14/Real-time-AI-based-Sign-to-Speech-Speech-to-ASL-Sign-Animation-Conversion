import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import webbrowser
import time
import threading


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDBACK_FILE = os.path.join(BASE_DIR, "feedback.txt")
SIGN_HTML = os.path.join(BASE_DIR, "sign_to_speech", "index.html")
DJANGO_DIR = os.path.join(BASE_DIR, "speech_to_sign")
DJANGO_APP = os.path.join(DJANGO_DIR, "speech_to_sign_app.py")  # Your custom file


def open_feedback_window(root):
    fb = tk.Toplevel(root)
    fb.title("Feedback")
    fb.geometry("400x300")
    fb.resizable(False, False)
    fb.configure(bg="#fafafa")
    tk.Label(fb, text="Share your feedback!", font=("Segoe UI", 12, "bold"), bg="#fafafa").pack(pady=10)
    text = tk.Text(fb, width=40, height=10, font=("Segoe UI", 10))
    text.pack(pady=10)
    def submit():
        feedback = text.get("1.0", tk.END).strip()
        if not feedback:
            messagebox.showwarning("Empty", "Please type your feedback before submitting.")
            return
        try:
            with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {feedback}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save feedback:\n{e}")
            return
        messagebox.showinfo("Thank You", "Feedback saved to feedback.txt")
        fb.destroy()
    tk.Button(fb, text="Submit Feedback", font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", command=submit).pack(pady=10)


def show_loading(msg):
    w = tk.Toplevel()
    w.title("Please wait")
    w.geometry("300x130")
    w.resizable(False, False)
    tk.Label(w, text=msg, font=("Segoe UI", 11)).pack(pady=15)
    w.update()
    return w


def run_sign_to_speech():
    if not os.path.exists(SIGN_HTML):
        messagebox.showerror("Error", f"Web app not found:\n{BASE_DIR}\\sign_to_speech\\index.html\n\nCreate this folder/file first.")
        return
    win = show_loading("Starting local web server...")
    def serve_html():
        try:
            # UPDATED: Changed to port 5501 as requested
            server_process = subprocess.Popen([sys.executable, "-m", "http.server", "5501"], cwd=BASE_DIR)
            time.sleep(2)
            win.destroy()
            webbrowser.open("http://127.0.0.1:5501/sign_to_speech/index.html")
            messagebox.showinfo("Success", "Sign→Speech running at:\nhttp://127.0.0.1:5501/sign_to_speech/index.html")
        except Exception as e:
            if 'win' in locals():
                win.destroy()
            messagebox.showerror("Server Error", str(e))
    threading.Thread(target=serve_html, daemon=True).start()


def run_speech_to_sign():
    if not os.path.exists(DJANGO_APP):
        messagebox.showerror("Error", f"App not found:\n{BASE_DIR}\\speech_to_sign\\speech_to_sign_app.py\n\nExpected: speech_to_sign/speech_to_sign_app.py")
        return
    win = show_loading("Starting Speech→Sign server...")
    def start_django():
        try:
            # FIXED: Direct execution without runserver args
            proc = subprocess.Popen(
                [sys.executable, DJANGO_APP],
                cwd=DJANGO_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            time.sleep(4)  # Wait for server startup
            win.destroy()
            webbrowser.open("http://127.0.0.1:8000/")
            messagebox.showinfo("Success", "Speech→Sign running at:\nhttp://127.0.0.1:8000/\n\nClose GUI to stop server.")
        except Exception as e:
            if 'win' in locals():
                win.destroy()
            messagebox.showerror("Server Error", f"Failed to start:\n{str(e)}\n\nCheck:\n1. venv activated\n2. pip install -r requirements.txt\n3. Port 8000 free")
    threading.Thread(target=start_django, daemon=True).start()



def main():
    root = tk.Tk()
    root.title("Sign & Speech Communication Launcher")
    root.geometry("1300x750")
    root.resizable(False, False)
    
    # Gradient background
    gradient = tk.Canvas(root, width=1300, height=750, highlightthickness=0)
    gradient.pack(fill="both", expand=True)
    colors = ["#A7C7E7", "#BFC8F8", "#C7F2E3", "#FFE2CC"]
    h = 750 // len(colors)
    for i, c in enumerate(colors):
        gradient.create_rectangle(0, i*h, 1300, (i+1)*h, fill=c, outline="")
    
    frame = ttk.Frame(gradient, padding=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Styles
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Big.TButton", font=("Segoe UI", 20, "bold"), padding=25)
    style.configure("Title.TLabel", font=("Segoe UI", 32, "bold"))
    
    # Title
    ttk.Label(frame, text="✋ ↔ 🎤 Sign & Speech Converter", style="Title.TLabel").pack(pady=40)
    
    # Buttons
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(pady=30)
    ttk.Button(btn_frame, text="✋ Sign → Speech", style="Big.TButton", command=run_sign_to_speech).grid(row=0, column=0, padx=50, pady=20)
    ttk.Button(btn_frame, text="🎤 Speech → Sign", style="Big.TButton", command=run_speech_to_sign).grid(row=0, column=1, padx=50, pady=20)
    
    # Info - UPDATED with new port
    ttk.Label(
        frame,
        text="📌 Sign→Speech: Local server (port 5501)\n📌 Speech→Sign: speech_to_sign_app.py (port 8000)",
        font=("Segoe UI", 13),
        justify="center",
        foreground="#444"
    ).pack(pady=20)
    
    # Floating buttons
    tk.Button(
        root, text="💬 Feedback", font=("Segoe UI", 12, "bold"),
        bg="#FFB6C1", command=lambda: open_feedback_window(root)
    ).place(relx=0.95, rely=0.95, anchor="se")
    
    tk.Button(
        root, text="❌ Exit", font=("Segoe UI", 11, "bold"),
        bg="#e53e3e", fg="white", command=root.destroy
    ).place(relx=0.05, rely=0.95, anchor="sw")
    
    root.mainloop()


if __name__ == "__main__":
    main()
