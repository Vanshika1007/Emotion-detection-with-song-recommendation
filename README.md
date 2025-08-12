# 🎵 Emotion Detection with Song Recommendation

An AI-powered application that detects a user's emotion from their facial expression or text input and suggests personalized songs to match the mood.  
This project combines **Computer Vision**, **Natural Language Processing**, and **Music Recommendation Systems** to enhance the listening experience.

---

## 📌 Features

- **Emotion Detection**: Detects emotions like *Happy, Sad, Angry, Neutral, Fear, Surprise, Disgust* from:
  - Live camera feed (facial expression analysis)
  - Text-based input (sentiment analysis)
- **Music Recommendation**:
  - Suggests songs from a curated dataset or Spotify API based on detected emotion.
  - Provides direct links to songs/playlists.
- **Real-Time Processing**:
  - Fast and accurate predictions using a trained ML/DL model.
- **Responsive Interface**:
  - Simple and user-friendly UI for both mobile and desktop.

---

## 🛠️ Tech Stack

### **Frontend**
- HTML, CSS, JavaScript / React (if applicable)

### **Backend**
- Python (Flask / Django / FastAPI)
- TensorFlow / Keras / PyTorch for emotion detection model
- OpenCV for image processing

### **APIs & Tools**
- Spotify API / YouTube API for music suggestions
- NumPy, Pandas, Scikit-learn for data processing
- Matplotlib / Seaborn for visualization (optional)

---

## 🚀 How It Works

1. **Input Emotion Source**  
   - Live camera captures user's face  
   - OR user enters text describing their mood

2. **Emotion Detection**  
   - **Facial Expression**: OpenCV detects face → ML/DL model predicts emotion  
   - **Text Input**: NLP sentiment analysis determines emotion

3. **Song Recommendation**  
   - Matches detected emotion with pre-defined music dataset or queries Spotify API
   - Displays recommended songs/playlists

4. **Enjoy the Music!** 🎧

---
## 🖼️ Screenshots

| Emotion Detection | Song Suggestions |
|-------------------|------------------|
| ![Detection](detection.png) | ![Songs](songs.png) |


## 📂 Project Structure

