from flask import Flask
from waitress import serve

app = Flask("__main__")

@app.route('/')
def index():
    return 'Hello, World! this is my base page'

@app.route('/profile/')
@app.route('/profile/<user_name>')
def profile(user_name ='guest'):
    return f'Welcome to the Profile Page! of {user_name}'

@app.route('/blog')
@app.route('/blog/<int:post_id>')
def blog(post_id=0):
    try:
        if post_id == 0:
            return 'No. is not even or odd'
        elif post_id % 2 == 0:
            return f'Post {post_id} is even'
        elif post_id % 2 == 1:
            return f'Post {post_id} is odd'
        else:
            return 'Please add a number to the url'
    except TypeError:
        return 'Please add a number to the url'
