import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" :question}]
    )
    
    return response

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    generated_image = response['data'][0]['url']
    return generated_image

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)