from flask import Flask, request, jsonify
import ContentGeneration.StoryGeneration as Sg
from google import genai
import os

app = Flask(__name__)

genaiClient = genai.Client(api_key=os.environ.get("GEMINI-API-KEY"))

@app.route("/generatestory", methods =['POST'])
def ReceivePrompt():
    try:
        #request.is_json checks if content type is application/json
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        requestBody = request.json
        UserPrompt = requestBody.prompt
        story = Sg.generateStory(UserPrompt)

        return jsonify({
            "status": "Story Generated Successfully",
            "story": story
        }), 200

    except Exception as e:
        return jsonify({
            "Status" : f"An Internal server error has occured",
            "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

