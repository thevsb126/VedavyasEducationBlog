from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Interested to learn about Deep Learning. Recommend me some good courses, please!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I have uploaded a new course on Udemy about 2D art. Check it out if it interests you!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
