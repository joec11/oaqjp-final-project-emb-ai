import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document" : { "text" : text_to_analyse } }

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers = headers)

    # Handle the case where the response is a bad request (e.g., blank input)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Extract emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extract individual emotion scores
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)

    # Create a dictionary with only the required emotions
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key = emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    # Return the emotion scores dictionary including the dominant emotion
    return emotion_scores
