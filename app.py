from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('emotion_model.pkl')

emotion_playlists = {
    "happy": [
        {"title": "Happy - Pharrell Williams", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"title": "Can't Stop the Feeling - Justin Timberlake", "url": "https://www.youtube.com/watch?v=ru0K8uYEZWw"},
    ],
    "sad": [
        {"title": "Someone Like You - Adele", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        {"title": "Let Her Go - Passenger", "url": "https://www.youtube.com/watch?v=RBumgq5yVrA"},
    ],
    "angry": [
        {"title": "Breaking the Habit - Linkin Park", "url": "https://www.youtube.com/watch?v=v2H4l9RpkwM"},
        {"title": "Smells Like Teen Spirit - Nirvana", "url": "https://www.youtube.com/watch?v=hTWKbfoikeg"},
    ],
    "calm": [
        {"title": "Weightless - Marconi Union", "url": "https://www.youtube.com/watch?v=UfcAVejslrU"},
        {"title": "River Flows in You - Yiruma", "url": "https://www.youtube.com/watch?v=7maJOI3QMu0"},
    ],
    "fear": [
        {"title": "Demons - Imagine Dragons", "url": "https://www.youtube.com/watch?v=mWRsgZuwf_8"},
        {"title": "Boulevard of Broken Dreams - Green Day", "url": "https://www.youtube.com/watch?v=Soa3gO7tL-c"},
    ],
    "surprise": [
        {"title": "Surprise Yourself - Jack Garratt", "url": "https://www.youtube.com/watch?v=9ZgFjHqz5Dg"},
        {"title": "A Sky Full of Stars - Coldplay", "url": "https://www.youtube.com/watch?v=VPRjCeoBqrI"},
    ],
    "neutral": [
        {'title': 'Weightless - Marconi Union (Relaxing Ambient)', 'url': 'https://www.youtube.com/watch?v=UfcAVejslrU'},
        {'title': 'Chill Lofi Beats – 1 Hour Mix', 'url': 'https://www.youtube.com/watch?v=5qap5aO4i9A'},
        {'title': 'Peaceful Piano by Ludovico Einaudi', 'url': 'https://www.youtube.com/watch?v=91UURaQwq3U'},
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict([text])[0].lower()
    playlist = emotion_playlists.get(prediction, [])
    return render_template('index.html', text=text, emotion=prediction.capitalize(), playlist=playlist)

if __name__ == '__main__':
    app.run(debug=True)
