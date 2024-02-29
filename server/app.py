from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'hello'

@app.route('/count/<int:parameter>')
def count(parameter):
   
    numbers = [str(i) for i in range(parameter)]
    return '\n'.join(numbers)

@app.route('/math/<int:x>/<string:operation>/<int:y>')
def math(x, operation, y):
    if operation == '+':
        return str(x + y)
    elif operation == '-':
        return str(x - y)
    elif operation == '*':
        return str(x * y)
    elif operation == '/':
        if y != 0:
            return str(float(x) / y) 
            return "Error: Division by zero"
    elif operation == '%':
        return str(x % y)
    elif operation == 'div':
        if y != 0:
            return str(float(x) / y)  
        else:
            return "Error: Division by zero"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
