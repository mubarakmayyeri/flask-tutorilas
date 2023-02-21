from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
  return '<p>Hello, World!</p>'

@app.route('/<name>')
def hello_user(name):
  return f'Hello <b>{escape(name)}!!</b>, How are you today?'