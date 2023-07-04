from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import json
from gpt_api_call import ask_gpt, generate_image, download_image
from generate_prompt import *
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/spectacular-storyteller', methods=['GET', 'POST'])
#@login_required
def storyteller():
    if request.method == 'POST':
        #file = request.files['picture']

        image_url = generate_image(format_prompt_image(request))
        response = ask_gpt(format_prompt_article(request))

        content = response.choices[0]['message']['content']
        content_lists = content.split('\n')

        return render_template('article.html', content=content_lists, date=datetime.today().strftime('%Y-%m-%d'), article_title=request.form['article-title'], image_url=image_url)

    return render_template('storyteller.html')

@views.route('/professional-bio', methods=['GET', 'POST'])
#@login_required
def bio():
    if request.method == 'POST':
        #file = request.files['picture']

        #image_url = generate_image(format_prompt_image(request))
        response = ask_gpt(format_prompt_bio(request))

        content = response.choices[0]['message']['content']
        content_lists = content.split('\n')

        return render_template('bio.html', content=content_lists)

    return render_template('bio-generator.html')

@views.route('/upload', methods=['POST'])
def upload():
    file = request.files['picture']
    # Process the uploaded file here (e.g., save it to a directory or perform any required operations)
    return render_template('next_page.html', filename=file.filename)
