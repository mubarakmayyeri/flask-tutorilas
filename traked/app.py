from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Welcome to Traked......</h1>'


@app.route('/welcome/<name>', methods=['GET', 'POST'])
def welcome(name):
  return f'<p>Hi {name}, how are you'