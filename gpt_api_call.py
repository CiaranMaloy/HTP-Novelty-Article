import openai
import os

LOCAL = True

if not LOCAL:
    try:
        OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
        openai.api_key = OPEN_AI_API_KEY
    except KeyError:
        OPEN_AI_API_KEY = "Token not available!"
        # or raise an error if it's not available so that the workflow fails
else:
    # Set up your OpenAI API credentials
    with open('open_ai_api_key.txt') as f:
        key = f.readlines()[0]
        openai.api_key = key


def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" :question}]
    )
    # response = openai.Completion.create(
    #     engine='text-davinci-003',
    #     prompt=question,
    #     max_tokens=3000,
    #     temperature=1.0,
    #     n=1,
    #     stop=None,
    #     timeout=15
    # )
    
    return response