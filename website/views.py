from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import json
from gpt_api_call import ask_gpt
from generate_prompt import format_prompt
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        file = request.files['picture']

        prompt = format_prompt(request)
        response = ask_gpt(prompt)

        content = response.choices[0]['message']['content']
        content_lists = content.split('\n')

        return render_template('article.html', content=content_lists, date=datetime.today().strftime('%Y-%m-%d'), article_title=request.form['article-title'], filename=file.filename)

    return render_template('home.html')

@views.route('/upload', methods=['POST'])
def upload():
    file = request.files['picture']
    # Process the uploaded file here (e.g., save it to a directory or perform any required operations)
    return render_template('next_page.html', filename=file.filename)
