from gpt_api_call import ask_gpt

def format_prompt_article(request):
    # info
    article_title = request.form['article-title']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    age = request.form['age']
    #email = request.form['email']
    occupation = request.form['occupation']
    birth_place = request.form['birth-place']
    text = request.form['key-details']

    # generates prompt
    prompt = "Generate a news article in the style of Waltham Forest Echo (https://walthamforestecho.co.uk/).\n"
    prompt += "This article should be for novelty and will be in the style of a local newspaper.\n"
    prompt += "The 'Article Basis' will be the input context and the basis for the content of the article.\n" 
    #prompt += "it will come from a third party who wants to send the article to the subject of the article.\n"
    prompt += "This article should be at least 500 words.\n"
    prompt += f"Article Title: {article_title}\n"
    prompt += "Information about the subject of the article:\n"
    prompt += f"Name: {first_name} {last_name}\n"
    prompt += f"Age: {age}\n"
    prompt += f"Occupation: {occupation}\n"
    prompt += f"Birth Place: {birth_place}\n\n"
    prompt += "Article Basis:\n"
    prompt += text + "\n"
    #prompt += "No slurs, hate speech, or defamatory statements should be present in this article."

    return prompt

def format_prompt_image(request):
    # info
    article_title = request.form['article-title']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    age = request.form['age']
    #email = request.form['email']
    occupation = request.form['occupation']
    birth_place = request.form['birth-place']
    text = request.form['key-details']

        # generates prompt
    #prompt = "Generate a hedaline image for a news article in the style of a local newspaper\n"
    #prompt += "it will come from a third party who wants to send the article to the subject of the article.\n"
    prompt = f"Title: {article_title}\n"
    prompt += f"Name: {first_name} {last_name}\n"
    prompt += f"Age: {age}\n"
    #prompt += f"Occupation: {occupation}\n"
    prompt += f"Birth Place: {birth_place}\n\n"
    prompt += text + "\n"

    # asks chatGPT how to format this so that it gets a good image out of 
    pre_prompt = "I would like to use the following text to generate a DALL-E prompt"
    pre_prompt += "Could you return me a prompt that I can use in the DALL-E image generator to generate me a useful image from the infromation below.\n"
    pre_prompt += "This image should be for novelty"
    pre_prompt += "===================================="
    pre_prompt += prompt

    prompt = ask_gpt(pre_prompt)
    prompt = prompt.choices[0]['message']['content']
    print(prompt)

    return prompt

