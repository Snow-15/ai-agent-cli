import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("Gemini API Key wasn't found")

client = genai.Client(api_key=api_key)


def generate_response(messages):

    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0,
        ),
    )
