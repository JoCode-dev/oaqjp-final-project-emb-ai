from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)

    if(emotions["dominant_emotion"] == None):
        return " Invalid text! Please try again!."

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}. ".format(emotions["anger"], emotions["disgust"], emotions["fear"], emotions["joy"], emotions["sadness"], emotions["dominant_emotion"])

@app.route("/")
def render_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)