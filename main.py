from flask import Flask

main = Flask(__name__)

@main.route('/')
def home():
    return f'<h1>Welcome</>'