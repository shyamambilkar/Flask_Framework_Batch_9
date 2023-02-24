from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return "Hello Welcome to Flask...!!"


@app.route('/flask')
def Hello_Flask():
    return 'Welcome to Python Flask Framework...!!'


@app.route('/python')
def hello_python():
    return 'Welcome to Python and Data Science..!!'


if __name__ == "__main__":
    app.run()
