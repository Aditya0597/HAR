from flask import *
from project import app
from project.com.dao import conn_db
from project.com.dao.dashboardDao import dashboard

sidebar = {'home': None, 'byactivity': None, 'bydate': None, 'byarea': None}


@app.route('/')
def index():
    sidebar['home'] = True
    sidebar['byactivity'] = False
    sidebar['bydate'] = False
    sidebar['byarea'] = False
    return render_template('register.html', sidebar=sidebar)


@app.route('/home')
def home():
    sidebar['home'] = True
    sidebar['byactivity'] = False
    sidebar['bydate'] = False
    sidebar['byarea'] = False
    conn = conn_db()
    cursor = conn.cursor()
    print(cursor.execute('SELECT * FROM restaurants'))
    return render_template('home.html', sidebar=sidebar)


@app.route('/byactivity', methods=['POST', 'GET'])
def byactivity():
    if request.method == 'GET':
        sidebar['home'] = False
        sidebar['byactivity'] = True
        sidebar['bydate'] = False
        sidebar['byarea'] = False
        return render_template('byactivity.html', tables=0, sidebar=sidebar)
    else:
        act = request.form.get('act')
        byact = dashboard()
        data = byact.empByActivity(act)
        print(data)
        sidebar['home'] = False
        sidebar['byactivity'] = True
        sidebar['bydate'] = False
        sidebar['byarea'] = False
        print(sidebar)
        return render_template('byactivity.html', tables=1, emps=data, sidebar=sidebar)


@app.route('/bydate', methods=['POST', 'GET'])
def bydate():
    if request.method == 'GET':
        sidebar['home'] = False
        sidebar['byactivity'] = False
        sidebar['bydate'] = True
        sidebar['byarea'] = False
        return render_template('bydate.html', tables=0, sidebar=sidebar)
    else:
        session_time = request.form.get('session')
        print(session_time)
        bydate = dashboard()
        data = bydate.empBySession(session_time)
        print(data)
        sidebar['home'] = False
        sidebar['byactivity'] = False
        sidebar['bydate'] = True
        sidebar['byarea'] = False
        print(sidebar)
        return render_template('bydate.html', tables=1, emps=data, sidebar=sidebar)


@app.route('/byarea', methods=['POST', 'GET'])
def byarea():
    if request.method == 'GET':
        sidebar['home'] = False
        sidebar['byactivity'] = False
        sidebar['bydate'] = False
        sidebar['byarea'] = True
        return render_template('byarea.html', tables=0, sidebar=sidebar)
    else:
        area = request.form.get('area')
        print(area)
        bydate = dashboard()
        data = bydate.empByArea(area)
        print(data)
        sidebar['home'] = False
        sidebar['byactivity'] = False
        sidebar['bydate'] = False
        sidebar['byarea'] = True
        print(sidebar)
        return render_template('byarea.html', tables=1, emps=data, sidebar=sidebar)
