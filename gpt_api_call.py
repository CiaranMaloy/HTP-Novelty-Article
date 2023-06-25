import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
openai.api_key = OPEN_AI_API_KEY

# if not LOCAL:
#     try:
#         OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
#         openai.api_key = OPEN_AI_API_KEY
#     except KeyError:
#         OPEN_AI_API_KEY = "Token not available!"
#         # or raise an error if it's not available so that the workflow fails
# else:
#     # Set up your OpenAI API credentials
#     with open('.API_KEY/open_ai_api_key.txt') as f:
#         key = f.readlines()[0]
#         openai.api_key = key


def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" :question}]
    )
    
    return response