# ✋ Hand Gesture-Based Application Control Using Computer Vision and Python

## 🧭 Overview

This project presents a **gesture-based application control system** using **MediaPipe** and **OpenCV**. Users can open and close applications using specific hand gestures detected in real-time through a webcam. The system is built using Python and deployed as a standalone desktop `.exe` application using PyInstaller.

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [System Workflow](#-system-workflow)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Deployment](#-deployment)
- [Screenshots](#-screenshots)

---

## ✅ Features

- 🖐 Real-time hand gesture recognition using MediaPipe
- 🧠 Specific gestures mapped to app control (e.g. 5 fingers = open Notepad)
- 🖥️ Open or close desktop applications programmatically
- 📦 One-click `.exe` file, no Python/VS Code needed after deployment
- 🔒 Lightweight and fully offline

---

## 🧰 Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- PyAutoGUI
- PyInstaller (for deployment)

---

## 🔁 System Workflow

1. Webcam captures live video feed.
2. MediaPipe detects hand and landmark positions.
3. Gestures are recognized based on finger states.
4. Actions like opening or closing applications are triggered.

---

## 🛠️ Installation

### 📌 Prerequisites

```bash
pip install opencv-python mediapipe pyautogui
