from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5052)