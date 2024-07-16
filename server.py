"""
Code By Brennan Mulligan
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")

def emotion_detect():
    """
    Detects the emotion of the given text.

    This function retrieves the text to analyze from the request arguments,
    passes the text to the emotion detection function, and returns a formatted
    response string with the detected emotions and dominant emotion.

    Returns:
        str: A formatted string with detected emotions and dominant emotion or
             an error message for invalid input.
    """
    # Retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is none, indicating an invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."

    # Get all items except the last one
    items = list(response.items())[:-1]

    # Create a list to store the formatted key-value pairs
    format_pairs = [f"'{key}': {value}" for key, value in items]

    # Join the list into a single string with the desired format
    emote = ", ".join(format_pairs[:-1]) + f" and {format_pairs[-1]}"
    dom = response['dominant_emotion']

    # Return the final formatted string
    return f"For the given statement, the system response is {emote}. The dominant emotion is {dom}"

# App Route
@app.route("/")
def render_index_page():
    """
    Renders Index Page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
