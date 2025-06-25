✋ Control Applications Using Hand Gestures with Python and Computer Vision  
🧭 Overview

This project presents a **real-time gesture recognition system** that allows users to control desktop applications using **hand gestures** captured from a webcam. It is built with **Python**, using **OpenCV** and **MediaPipe**, and can be compiled into a standalone `.exe` application — no need to install Python!

📊 Hand Gestures

The system supports gesture recognition such as:

- 🖐️ **Five fingers** → Open Notepad
- ✊ **No fingers** (fist) → Close Notepad

You can modify `main.py` to support more gestures or actions.

🧠 System Architecture

- 📷 Webcam input using OpenCV
- 🤖 Hand detection & landmark tracking using MediaPipe
- ✋ Custom logic to count fingers
- ⚙️ System automation using PyAutoGUI

🧪 Sample Results

- Detected 5 fingers → ✅ Launched Notepad  
- Detected fist → ✅ Closed Notepad

🚀 Deployment

This app has been converted to `.exe` using PyInstaller.

🔗 **Download the EXE:**  
👉 [Click here to download `main.exe`](https://drive.google.com/uc?id=YOUR_FILE_ID&export=download)

🛠️ Manual Build (Developer):

```bash
pyinstaller --noconsole --onefile main.py --add-data "C:/path/to/tflite.tflite;mediapipe/modules/..." --add-data ...
