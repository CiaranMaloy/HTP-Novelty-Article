# generate prompt file

#prompt structure:


def format_prompt(information):
    # info
    first_name = information['firstName']
    last_name = information['secondName']
    text = information['prompt']

    # generates prompt
    prompt = "Write a news article about the person below.\n"
    prompt += "This article should be for novelty and will be in the style of a local newspaper.\n"
    prompt += "The 'Article Basis' will be the input context and the basis for the content of the article, it will come from a third party who wants to send the article to the subject of the article.\n"

    prompt += "Infromation about the subject of the article:"
    prompt += f"Name: {first_name} {last_name}\n"
    #prompt += f"Age: {age}\n"
    #prompt += f"Occupation: {occupation}\n"
    #prompt += f"Birth Place: {birth_place}\n\n"
    prompt += "Article Basis:\n"
    prompt += text

    return prompt