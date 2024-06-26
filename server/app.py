#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route('/count/<int:integer>')
def count(integer):
    result = '\n'.join(str(num) for num in range(integer))
    return result + '\n'

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = 0

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2

    final = str(result)
    return final

if __name__ == '__main__':
    app.run(port=5555, debug=True)
