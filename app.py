from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World222!'


@app.route('/test')
def test():
    return test2(ll=1, l222=3)


def test(values: dict):
    for key in values.keys():
        print(key)
        print(values[key])

    return 'complete'


def test2(**kwargs):
    return test(kwargs)


values = {
    'a': 123
}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
