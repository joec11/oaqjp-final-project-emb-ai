''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows each emotion score
        and the dominant emotion for the provided text.
    '''

    # Get the input text from the HTML request
    text_to_analyze = request.args.get('textToAnalyze')

    # If no text is provided, return an error message
    if not text_to_analyze:
        return "No text provided! Please enter some text."

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores from the response
    try:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']
    except (TypeError, KeyError):
        return "Invalid input or response format! Try again."

    # Construct and return the result string
    return (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}.<br>"
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
