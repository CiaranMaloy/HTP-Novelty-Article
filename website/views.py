from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
#from .models import *
#from . import db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        #email = request.form.get('email')
        #first_name = request.form.get('firstName')
        #password1 = request.form.get('secondName')
        #password2 = request.form.get('password2')

        # password and credentials logic
        #user = User.query.filter_by(email=email).first()

            # add usere to database
        #flash('Account created', category='success')
        return render_template('article.html')

    return render_template('home.html')


