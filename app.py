from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
def greet():
    return 'Hello'

@app.route('/greet/<name>')
def greet_name(name):
    return f'Hello {name}'

@app.route('/convert/<celsius>')
def convert_temp(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = celsius * 9 / 5 + 32
        return f'{celsius} Celsius is {fahrenheit} Fahrenheit'
    except ValueError:
        return 'Invalid input: Please enter a number.'

if __name__ == '__main__':
    app.run(debug=True)
