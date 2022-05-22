from . import db
from .models import User, Snippet
from flask import Blueprint, jsonify, render_template, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from rpack import *

views = Blueprint('views', __name__)

#----------------------------------------------------------------------------#
#FIXED/CONSTANT PAGES

@views.route('/')
def first_landing():
    return render_template("landing.html")

@views.route('/enter')
def user_auth():
    return render_template("log_or_sign.html")

@views.route('/welcome')
@login_required
def welcome_user():
    return render_template("welcome.html")

@views.route('/message')
@login_required
def see_message():
    return render_template("message.html")

@views.route('/options', methods=['GET', 'POST'])
@login_required
def theme_options():
    return render_template("options.html")

#----------------------------------------------------------------------------#
#THESE PAGES SHOULD ALL HAVE SIMILAR FUNCTIONALITIES

@views.route('/literature', methods=['GET', 'POST'])
@login_required
def literature():
    subthemes = ['feminist literature', 'queer love letters', 'top horror novels turned to movies','top 10 fanfictions','most tear-jerking poems']
    all_information = []
    for subtheme in subthemes:
        returned_value = set_up_page(subtheme)
        if isinstance(returned_value, list):
            newUrls = returned_value
            paragraphs = find_multiple_info(newUrls)
            all_information.append(paragraphs)
        else:
            url = returned_value
            information = find_info(url)
            all_information.append(information)
    return render_template("literature.html", all_information=all_information)

@views.route('/art', methods=['GET', 'POST'])
@login_required
def art():
    return render_template("art.html")

@views.route('/music', methods=['GET', 'POST'])
@login_required
def music():
    
    return render_template("music.html")

@views.route('/tech', methods=['GET', 'POST'])
@login_required
def tech():
    return render_template("tech.html")

#----------------------------------------------------------------------------#
#PAGE FOR SEEING SEARCH FINDINGS + MAKING SNIPPETS

texts = ["dummy text 1", "dummy text 2"]

@views.route('/info', methods=['GET', 'POST'])
@login_required
def snip_and_sip(): #lolol sorry but this is too funny
    if request.method == 'POST':
        snipText = request.form.get('snip_text')
        if len(snipText) < 5:
            flash('This snippet is too small!', category='error')
        else:
            newSnippet = Snippet(snipText=snipText, user_name=current_user.username)
            db.session.add(newSnippet)
            db.session.commit()
            return render_template("info.html", user=current_user)
    else:
        texts = ['dummy text 1', 'dummy text 2']
    return render_template("info.html", user=current_user, texts=texts)

#----------------------------------------------------------------------------#

@views.route('/my-snippets') #no POST because POST is done from the pages above
def show_snippets():
    snippets = Snippet.query.all()
    return render_template("my_snippets.html", user=current_user, snippets=snippets)