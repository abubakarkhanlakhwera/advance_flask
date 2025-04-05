from flask import Flask ,url_for
from waitress import serve

app = Flask("__main__")
@app.route('/')
def index():
    return 'Hello, World! this is my base page'

@app.route('/home/<username>')
def home(username):
    return f'Welcome to the Home Page! {username}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('home',username='John Elton'))
    print(url_for('home',username='John Elton',password='1234'))
    