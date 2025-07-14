
#  Offline Scam Message & Link Checker

A simple, offline Python GUI application that analyzes text messages and links to detect potential scams using heuristics like keywords and suspicious domains.

---

##  Features

- Detects scam messages based on common phishing keywords.
- Analyzes URLs for suspicious domains.
- Color-coded risk score (Safe / Warning / High Risk).
- Simple Tkinter GUI for user interaction.
- Works **100% offline** — no data leaves your device.

---

##  How It Works

The application:
- Uses a keyword-based scoring system (e.g. "lottery", "claim", "urgent").
- Extracts URLs and checks for risky patterns or domains.
- Assigns a scam risk score (0–10) based on the content.
- Shows results in a clear, scrollable output box with color tags.

---

##  Tech Stack

- Python 3.x
- Tkinter (for GUI)
- `re` for regular expressions
- `urllib.parse` for URL parsing

---

##  Installations

1. **Clone the repository**
```bash
git clone https://github.com/your-username/scam-checker-python.git
cd scam-checker-python
```

2. **(Optional) Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
python scam_checker.py
```

---

##  Requirements

No external libraries required — runs with default Python libraries.


## Future Improvements

- Add Ai to make advanced predictions
- Create a web or mobile version
- Support for multilingual scam detectin

---

##  About the Author

This project was created by a high school student passionate about cybersecurity and computer science. It was built as a social impact project to stop people from becoming victims of phishing/scams. 

## Related Blog Post

I wrote a detailed blog about how I built this project, including the challenges and lessons I learned.

➡️ [Read it on Medium]( Related Blog Post

I wrote a detailed blog about how I built this project, including the challenges and lessons I learned.

➡️ [Read it on Medium](https://medium.com/@rajanenim/how-i-built-a-scam-message-and-link-checker-tool-using-python-14e1b4ad1fe6)
)


##  License

This project is open-source and available under the [MIT License](LICENSE).
