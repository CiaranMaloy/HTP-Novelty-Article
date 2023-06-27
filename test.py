import requests
import openai
import os
from dotenv import load_dotenv

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
        size="1024x1024"
    )
    generated_image = response['data'][0]['url']
    return generated_image

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

prompt = input("Input your text:")
generated_image = generate_image(prompt)

# Save image url to into file
image_url = generated_image
save_path = 'image.jpg'
download_image(image_url, save_path)