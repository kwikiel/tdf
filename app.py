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


if __name__ == "__main__":
    app.run()
