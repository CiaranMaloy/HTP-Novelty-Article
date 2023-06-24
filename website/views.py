from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import json
from gpt_api_call import ask_gpt
from generate_prompt import format_prompt

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        prompt = request.form.get('prompt')

        information = {
            'firstName': first_name,
            'secondName': second_name,
            'prompt': prompt
        }
        prompt = format_prompt(information)
        response = ask_gpt(prompt)


        print(response.choices[0].text.strip())

        return render_template('article.html', content=response.choices[0].text.strip())

    return render_template('home.html')


