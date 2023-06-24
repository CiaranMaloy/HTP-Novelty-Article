import openai

# Set up your OpenAI API credentials
with open('open_ai_api_key.txt') as f:
    key = f.readlines()[0]
    openai.api_key = key

def ask_gpt(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    
    return response

# Ask a question and get a response
user_question = input("Ask a question: ")
response = ask_gpt(user_question)
print(response)
print('\n')
print(response.choices[0].text.strip())