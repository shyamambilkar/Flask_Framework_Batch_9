from os import name
import os
from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def Hello_World(name):
    return 'Hello %s!'%name, 'Welcome to Data Science Class...!!'


if __name__ == "__main__":
    app.run(port=5010, host= '0.0.0.0' )
