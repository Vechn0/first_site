from app import app

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/info")
def info():
    return "This is an information page"


@app.route("/reverse/<text>")
def reverse(text):
    return text[::-1]

@app.route("/user/<name>/<int:age>")
def user(name,age):
    return f"Hello,{name}, you are {age} years old"

@app.route("/calc/<int:a>/<int:b>")
def clac(a,b):
    return str(a+b)
