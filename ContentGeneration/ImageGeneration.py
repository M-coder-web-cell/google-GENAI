from google.genai import types
from app import genaiClient as client
import json

def createImageGenerationPrompt( rawImgPrompt : str):
    with open("systemInstructionforImage.txt", "r") as file:
        systemInstructionforImage = json.load(file)

    response = client.models.generate_content(
        model ="gemini-1.5-flash",
        contents = rawImgPrompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction = systemInstructionforImage['image'],
            response_mime_type = "application/json",
            response_schema={
                "type": "OBJECT",
                "properties":{
                    "imagePrompt":{"type":"STRING"}
                }
            }
        )
    )
    return response.imagePrompt

def createImages( prompt : str, number : int):
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images= number,
        )
    )
    return response