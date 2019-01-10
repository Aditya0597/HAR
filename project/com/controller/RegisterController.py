from flask import *
from project import app
from project.com.dao import conn_db

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')
def home():
    conn=conn_db()
    cursor=conn.cursor()
    print(cursor.execute('SELECT * FROM restaurants'))
    return render_template('home.html')