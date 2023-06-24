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
        prompt = format_prompt(request)
        response = ask_gpt(prompt)

        content = response.choices[0]['message']['content']
        content_lists = content.split('\n')

        return render_template('article.html', content=content_lists)

    return render_template('home.html')


