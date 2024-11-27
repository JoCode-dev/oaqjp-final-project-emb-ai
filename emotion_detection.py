import requests

def emotion_detector(text_to_analyse):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=URL, json=myobj, headers=headers)

    return response.text