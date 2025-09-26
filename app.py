"""Главный модуль Flask-приложения."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
# первая функция
def hello():
    """Возвращает приветствие на главной странице."""
    return "Hello,Flask!"


@app.route('/')
def home():
    return 'This is the home page'


@app.route('/about')
def about():
    return 'About page'


@app.route('/contact')
def contact():
    return 'Contact page'


@app.route('/greet/<name>')
def helli_name(name):
    return f'Hello {name}!'


@app.route('/user/<int:id>')
def user_id(id: int) -> str:
    return f'User ID : {id}'


@app.route('/info')
def info():
    return 'This is the info page'


@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1,num2):
    return f'The sum of {num1} and {num2} is {num1+num2}'

@app.route('/reverse/<str:message>')
def reverse_message(message):
    return message[0:0-1]

@app.route('/user/<str:name>/<int:age>')
def user_info(name,age):
    return f'Hello, {name}! You are {age} years old'

if __name__ == '__main__':
    app.run(debug=True)
