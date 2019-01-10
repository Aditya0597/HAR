from flask import *
from project import app
from project.com.dao import conn_db


@app.route('/logout')
def logout():
    return render_template('login.html')
