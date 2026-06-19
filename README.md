# ✋ Finger Counter using OpenCV & MediaPipe

A real-time Computer Vision project that detects a hand through a webcam and counts the number of fingers raised using OpenCV and MediaPipe.

## 📌 Overview

This project uses MediaPipe Hand Tracking to identify hand landmarks and determine how many fingers are extended. The finger count is displayed live on the webcam feed.

The application demonstrates the fundamentals of hand tracking, landmark detection, and gesture analysis in real-time.

## 🚀 Features

* Real-time webcam feed
* Hand detection using MediaPipe
* 21 hand landmark tracking
* Live finger counting (0–5)
* Visual display of hand landmarks and connections
* Real-time finger count overlay

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe

## 📂 Project Structure

```bash
finger-counter/
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/finger-counter.git
cd finger-counter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-python mediapipe
```

## ▶️ Running the Project

```bash
python main.py
```

Press **Q** to exit the application.

## 🧠 How It Works

1. OpenCV captures video from the webcam.
2. MediaPipe detects the hand and extracts 21 landmark points.
3. The program compares fingertip positions with lower finger joints.
4. Extended fingers are counted.
5. The total count is displayed on the screen in real time.

## 📸 Output

The application displays:

* Hand landmarks
* Hand connections
* Number of fingers detected

Example:

```text
✊  -> 0 Fingers
☝️  -> 1 Finger
✌️  -> 2 Fingers
🖖 -> 4 Fingers
🖐️ -> 5 Fingers
```

## 🎯 Learning Outcomes

Through this project, I learned:

* Real-time video processing with OpenCV
* Hand tracking using MediaPipe
* Landmark-based gesture recognition
* Computer Vision fundamentals
* Real-time object detection workflows

## 👩‍💻 Author

**Kritika Raghav**

B.Tech CSE (AI & Data Science)
Poornima University, Jaipur

GitHub: https://github.com/ykrtika6767
LinkedIn: https://www.linkedin.com/in/kritika-raghav-741b63290/
