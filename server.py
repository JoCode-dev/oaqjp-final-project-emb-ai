from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)

    return f"For the given statement, the system response is 'anger': {emotions["anger"]}, 'disgust': {emotions["disgust"]}, 
    'fear': {emotions["fear"]}, 'joy': {emotions["joy"]} and 'sadness': {emotions["sadness"]}. The dominant emotion is {emotions["dominant_emotion"]}. "

@app.route("/")
def render_index():
    return render_template("index.html")