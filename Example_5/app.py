from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_students():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            fname = request.form['fname']
            lname = request.form['lname']
            address = request.form['address']
            email = request.form['email']
            mobile = request.form['mobile']
            designation = request.form['designation']

            with sql.connect('database.db') as con:
                cur = con.cursor()

            cur.execute('INSERT INTO students(fname,lname,address,email,mobile,designation) VALUES (?,?,?,?,?,?)',
                        (fname, lname, address, email, mobile, designation))

            con.commit()
            msg = "Record added Successfully...!!"
        except:
            con.rollback()
            msg = 'Error in Insert Operation...!!'

        finally:
            return render_template('result.html', msg=msg)


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from students')

    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True, port=5052)
