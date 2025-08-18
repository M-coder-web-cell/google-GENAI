from google.genai import types
from app import genaiClient as client
import json,os



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
    return response

def createImages( prompt : str, number : int):
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images= number,
        )
    )
    return response

imagenPrompt ="Professional product photography of a small, hand-carved wooden rhino sculpture from Assam. The rhino is carved from a single piece of rich, dark mango wood, showcasing intricate chisel marks and a smooth, polished finish. It is placed on a clean, rustic slice of teak wood with a soft-focus, bokeh background of lush green foliage. The scene is bathed in soft, natural morning light, creating gentle highlights on the rhino's form and casting a soft shadow. Close-up shot, rule of thirds composition, photorealistic, hyper-detailed, sharp focus, 8K."

def main():
    createImages(imagenPrompt, 2)


if __name__ == "__main__":
    main()