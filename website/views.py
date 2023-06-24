from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import *
from . import db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('secondName')
        password2 = request.form.get('password2')

        # password and credentials logic
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('firstname must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters', category='error')
        else: 
            #new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            #db.session.add(new_user)
            #db.session.commit()

            # add usere to database
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template('home.html')


