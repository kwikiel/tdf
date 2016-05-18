import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash, jsonify

# config
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'keksecret'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()


@app.route('/')
def show_entries():
    """ Seek DB for entries, returns them """
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template("index.html", entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ User login/auth/session mgmt"""
    error = None
    if request.method = "POST":
        if request.form['username'] == app.config['USERNAME'] \
                and request.form['password'] == app.config['PASSWORD']:
                    session['logged_in'] = True
                    flash("You were logged in")
                    return redirect(url_for("index"))
    else:
        error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route('/logout')
def logout():
    """ User mgmt """
    session.pop('logged_in', None)
    flash("you were logged out")
    return redirect(url_for('index'))


if __name__ == "__main__":
    init_db()
    app.run()
