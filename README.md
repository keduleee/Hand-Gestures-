**Control Applications Using Hand Gestures with Python and Computer Vision**

Overview

This project presents a **real-time gesture recognition system** that allows users to control desktop applications using **hand gestures** captured from a webcam.  
It is built with **Python**, using **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

---

Hand Gestures

The system supports gesture recognition such as:

- 🖐️ **Five fingers** → Open Notepad  
- ✋ **Fist (0 fingers)** → Close all apps  
- ✌️ **Two fingers** → Open Calculator  
- 🤟 **Three fingers** → Open Microsoft Excel  
- ✌️✌️ **Four fingers** → Open Microsoft Word


 Sample Results

- Detected 5 fingers → ✅ Opened Notepad  
- Detected 4 fingers → ✅ Opened Microsoft Word  
- Detected 3 fingers → ✅ Opened Microsoft Excel  
- Detected 2 fingers → ✅ Opened Calculator  
- Detected 0 fingers → ✅ Closed all apps (Notepad, Word, Excel, Calculator)

---
 How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gesture-control-app.git
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Perform gestures in front of the webcam:

   | Finger Count | Action                      |
   |--------------|-----------------------------|
   | 5            | Open Notepad                |
   | 4            | Open Microsoft Word         |
   | 3            | Open Microsoft Excel        |
   | 2            | Open Calculator             |
   | 0            | Close all running apps      |


Common App Commands

   | Application   | Open Command     | Close Command                       |
   | ------------- | ---------------- | ----------------------------------- |
   | Google Chrome | `start chrome`   | `taskkill /im chrome.exe /f`        |
   | Spotify       | `start spotify`  | `taskkill /im spotify.exe /f`       |
   | Paint         | `start mspaint`  | `taskkill /im mspaint.exe /f`       |
   | File Explorer | `start explorer` | *Not recommended to close manually* |
   | WordPad       | `start wordpad`  | `taskkill /im wordpad.exe /f`       |
 Make sure the application is installed and accessible via command line (start) before using it.


