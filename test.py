import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

def ask_gpt(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    
    return response.choices[0].text.strip()

# Ask a question and get a response
user_question = input("Ask a question: ")
response = ask_gpt(user_question)
print(response)