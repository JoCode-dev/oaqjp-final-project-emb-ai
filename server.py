"""
Flask server
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def handle_emotion_detector():
    """
    Get the text to Analyse
    Return scores and the dominant emotion
    """

    # Get the text to analyze
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)

    if emotions["dominant_emotion"] is None:
        return " Invalid text! Please try again!."

    response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response

@app.route("/")
def render_index():
    """
    Return the index.html page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
