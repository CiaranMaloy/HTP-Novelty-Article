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

def format_prompt_bio(request):
    # info
    #article_title = request.form['article-title']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    age = request.form['age']
    #email = request.form['email']
    occupation = request.form['occupation']
    birth_place = request.form['birth-place']
    text = request.form['key-details']
    employment_history = request.form['employment-history']

    # generates prompt
    prompt = "Generate a professional bio for a person of interest, this bio should be in long form and be suitable for use in professional environments such as websites and linkedin.\n"
    prompt += "This bio should be written such that it talks up a persons achievements slightly in a way that a human would not write about himself or herself, while still staying completely true to the base material and realistic.\n"
    prompt += "The 'Base Material' will be the input context and the basis for the content of the bio.\n" 
    #prompt += "it will come from a third party who wants to send the article to the subject of the article.\n"
    prompt += "This bio should be at least 500 words.\n"
    prompt += "Information about the subject of the bio:\n"
    prompt += f"Name: {first_name} {last_name}\n"
    prompt += f"Age: {age}\n"
    prompt += f"Occupation: {occupation}\n"
    prompt += f"Birth Place: {birth_place}\n\n"
    prompt += f"Employment History:\n"
    prompt += employment_history + "\n"
    prompt += "Base Material - THIS SHOULD BE MENTIONED WITH IMPORTANCE WITHIN THE BIO:\n"
    prompt += text + "\n"
    #prompt += "No slurs, hate speech, or defamatory statements should be present in this article."

    return prompt

def format_prompt_cv(request):
    # info
    #article_title = request.form['article-title']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    age = request.form['age']
    #email = request.form['email']
    occupation = request.form['occupation']
    current_location = request.form['current-location']
    text = request.form['key-details']
    employment_history = request.form['employment-history']
    target_roles = request.form['target-roles']
    base_intro = request.form['base-intro']

    # generates prompt
    prompt = "Generate a short and easy to understand introductory paragraph to a CV, this should be for use in a professional setting.\n"
    #prompt += "This introduction should be written such that it talks up a persons achievements slightly in a way that a human would not write about himself or herself, slightly, but not too much, British english, not american english.\n"
    #prompt += "The '' will be the input context and the basis for the content of the bio.\n" 
    #prompt += "it will come from a third party who wants to send the article to the subject of the article.\n"
    #prompt += "This bio should be at least 500 words.\n"
    prompt += "Information about the subject of the CV intro:\n"
    prompt += f"Name: {first_name} {last_name}\n"
    prompt += f"Age: {age}\n"
    prompt += f"Occupation: {occupation}\n"
    prompt += f"Currently resides in: {current_location}\n\n"
    prompt += f"Employment History:\n"
    prompt += employment_history + "\n"
    prompt += "Key Details - These are details that should be mentioned with importance:\n"
    prompt += f"Key Details:{text}\n\n"
    #prompt += "No slurs, hate speech, or defamatory statements should be present in this article."

    prompt += "Target role(s) - IMPORTANT - this is the job role or title that the user wants to be applying for the output should be written with the aim of ataining this job, or this type of job."
    prompt += "Anything not relating to this role, should be kept out of the introduction and assumed to be part of the body of the CV:"
    prompt += f"Target Role(s): {target_roles}\n\n"

    prompt += "As an example, here is what the user currently has for his/her CV, use the content at will, this should be an example of what to output:\n"
    prompt += f"Example/existing intro: {base_intro}\n"

    prompt += "--------------------"
    prompt += "This should be written as if the user is writing it."
    prompt += "This should be in thre formal style."
    prompt += "This is being used to apply for jobs in ther UK."

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

