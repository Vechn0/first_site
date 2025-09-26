from app import app


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
    try:
        return f'The sum of {num1} and {num2} is {num1+num2}'
    except ValueError:
        print("Введите корректное число!")

@app.route('/reverse/<message>')
def reverse_message(message):
    if len(message) < 2:
        return 'Слишком короткое сообщение!'
    return message[0:0-1]

@app.route('/user/<name>/<int:age>')
def user_info(name,age):
    if age < 0:
        return f'Вы ввели неправильный возраст'
    else:
        return f'Hello, {name}! You are {age} years old'
