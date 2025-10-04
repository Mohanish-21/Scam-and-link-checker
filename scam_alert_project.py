
import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from urllib.parse import urlparse

# -------------------- SCAM DETECTION LOGIC --------------------
def detect_scam(text):
    scam_keywords = [
        "lottery", "prize", "won", "you have been selected", "click here",
        "claim", "money", "reward", "gift", "urgent", "free", "cash", "limited time","Fast","instaant","Only today"," Scholarship", 
    ]
    suspicious_domains = [".xyz", ".win", ".top", ".buzz", ".click", ".loan", ".vip", ".info",".onion "]

    score = 0
    text_lower = text.lower()

    for keyword in scam_keywords:
        if keyword in text_lower:
            score += 2

    urls = re.findall(r'https?://[^\s]+', text)
    for url in urls:
        parsed = urlparse(url)
        if any(ext in parsed.netloc for ext in suspicious_domains):
            score += 3
        if "free" in url or "prize" in url or "login" in url:
            score += 2

    # Scoring results
    if score >= 7:
        return " High Risk: This message or link is likely a scam.", "red", score
    elif 4 <= score < 7:
        return " Warning: This may be a scam. Be cautious.", "orange", score
    else:
        return " Safe: No strong signs of a scam were detected.", "green", score

# -------------------- BUTTON FUNCTION --------------------
def analyze_input():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showinfo("Input Needed", "Please enter a message or link to check.")
        return

    result, color, score = detect_scam(user_input)
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f" Scam Risk Score: {score}/10\n\n", "header")
    output_box.insert(tk.END, result, "status")
    output_box.tag_config("status", foreground=color, font=("Arial", 13, "bold"))
    output_box.tag_config("header", font=("Arial", 12, "bold"))
    output_box.config(state='disabled')

# -------------------- GUI SETUP --------------------
def run_gui():
    global input_box, output_box

    window = tk.Tk()
    window.title(" Offline Scam Message & Link Checker")
    window.geometry("720x560")
    window.config(bg="#e6f2ff")  # Light blue

    tk.Label(window, text="Enter a message or website link to check for scams:",
             font=("Arial", 14, "bold"), bg="#e6f2ff").pack(pady=10)

    input_box = scrolledtext.ScrolledText(window, width=80, height=6, font=("Arial", 12))
    input_box.pack(padx=10, pady=5)

    tk.Button(window, text=" Analyze", command=analyze_input,
              font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)

    tk.Label(window, text="Analysis Result:",
             font=("Arial", 14, "bold"), bg="#e6f2ff").pack()

    output_box = scrolledtext.ScrolledText(window, width=80, height=12,
                                           font=("Arial", 12), bg="#f9f9f9", state='disabled')
    output_box.pack(padx=10, pady=10)

    window.mainloop()

# -------------------- RUN THE APP --------------------
if __name__ == "__main__":

    run_gui()
