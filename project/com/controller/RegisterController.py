from flask import *
from project import app
from project.com.dao import conn_db

@app.route('/')
def index():
    conn=conn_db()
    cursor=conn.cursor()
    print(cursor.execute('SELECT * FROM restaurants'))
    return render_template('home.html')