from google import genai
from google.genai import types
import os
from app import genaiClient as client


def generateStory( UserPrompt : str):
    with open('systemInstruction.txt', "r") as file:
        systemInstruction = file.read()

    response = client.models.generate_content(
        model ="gemini-1.5-flash",
        contents = UserPrompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction = systemInstruction,
            response_mime_type = "application/json",
            response_schema={
                "type": "OBJECT",
                "properties":{
                    "story":{"type":"STRING"}
                }
            }
        )
    )
    return response