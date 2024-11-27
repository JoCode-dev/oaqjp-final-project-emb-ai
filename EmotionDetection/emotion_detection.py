import requests
import json
import operator


def emotion_detector(text_to_analyse):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=URL, json=myobj, headers=headers)
    res_json = json.loads(response.text)

    anger_score = res_json["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = res_json["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = res_json["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = res_json["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = res_json["emotionPredictions"][0]["emotion"]["sadness"]
    

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = max(scores.items(), key=operator.itemgetter(1))[0]

    result = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }

    return result