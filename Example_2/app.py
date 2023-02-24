from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


@app.route('/result')
def result():
    dict = {'Marathi': 50, 'English': 60, 'Physics': 75, 'Chemistry': 60, 'Biology':45}
    return render_template('result.html', result=dict)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
