from flask import Flask
from waitress import serve

app = Flask("__main__")

@app.route('/')
def index():
    return 'Hello, World! this is my base page'

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

def blog():
    return 'Welcome to the Blog Page!'
app.add_url_rule('/blog', blog,blog)
if __name__ == '__main__':
    app.run(debug=True)
