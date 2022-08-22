from urllib import request
from . import app
from flask import render_template, session, request
from .models import ViewPost

@app.route('/')
def HomeView():
    return render_template('home.html', user="Guest")

@app.route('/<post_id>')
def PostView(post_id):
    post = ViewPost(post_id)
    return render_template('home.html', user="Guest", post = post)


@app.route('/create', methods=['GET', 'POST'])
def CreateBlogView():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass 
    else:
        pass

