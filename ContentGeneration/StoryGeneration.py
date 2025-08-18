from google import genai
from google.genai import types
import os
from app import genaiClient as client
import json


def generateStory( UserPrompt : str):
    with open('ContentGeneration/SystemInstruction.json', "r") as file:
        system_instruction_data = json.load(file)

    response = client.models.generate_content(
        model ="gemini-1.5-flash",
        contents = UserPrompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction = system_instruction_data["story"],
            response_mime_type = "application/json",
            response_schema={
                "type": "OBJECT",
                "properties":{
                    "story":{"type":"STRING"}
                }
            }
        )
    )
    response_text = response.text #returns the raw 
    story_data = json.loads(response_text)  #converts this raw json string to dictionary
    return story_data['story']