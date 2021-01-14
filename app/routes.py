from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rahul'}

    posts = [ { 'author': {'username': 'John'},
                'body': 'Beutiful day in Indaiatuba!' },
              
              { 'author': {'username': 'Susan'},
                'body': 'Yoda is so cool!' }
            ]

    return render_template('index.html', title='Home', user=user, posts=posts)

