#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print('hello')
    return f'{parameter}'
    
@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Initialize the error variable as None
    error = None
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            error = "Cannot divide by zero"
        else:
            result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            error = "Cannot divide by zero"
        else:
            result = num1 % num2
    else:
        error = "Invalid operation"

    # If there's an error, return the error message and status code
    if error:
        return error, 400
    
    # Return the result as a string if no error occurred
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
