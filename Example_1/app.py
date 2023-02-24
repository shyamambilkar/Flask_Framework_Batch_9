from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def my_login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)