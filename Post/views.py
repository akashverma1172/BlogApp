from urllib import request
from . import app
from flask import render_template, session, request
from .models import ViewPost

@app.route('/')
def HomeView():
    posts = ViewPost()
    return render_template('home.html', user="Guest", posts = posts)


@app.route('/create', methods=['GET', 'POST'])
def CreateBlogView():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass 
    else:
        pass

