from flask import *
from project import app
from project.com.dao import conn_db
from project.com.dao.dashboardDao import dashboard

sidebar = {'home': None, 'byactivity': None, 'bytime': None, 'byarea': None}


@app.route('/')
def index():
    sidebar['home'] = True
    sidebar['byactivity'] = False
    sidebar['bytime'] = False
    sidebar['byarea'] = False
    return render_template('home.html', sidebar=sidebar)


@app.route('/home')
def home():
    sidebar['home'] = True
    sidebar['byactivity'] = False
    sidebar['bytime'] = False
    sidebar['byarea'] = False
    conn = conn_db()
    cursor = conn.cursor()
    print(cursor.execute('SELECT * FROM restaurants'))
    return render_template('home.html', sidebar=sidebar)


@app.route('/byactivity',methods=['POST','GET'])
def viewActivity():
    if request.method=='GET':
        sidebar['home'] = False
        sidebar['byactivity'] = True
        sidebar['bytime'] = False
        sidebar['byarea'] = False
        return render_template('byactivity.html', tables=0, sidebar=sidebar)
    else:
        act=request.form.get('act')
        byact=dashboard()
        data=byact.empByActivity(act)
        print(data)
        sidebar['home'] = False
        sidebar['byactivity'] = True
        sidebar['bytime'] = False
        sidebar['byarea'] = False
        print(sidebar)
        return render_template('byactivity.html', tables=1, emps=data, sidebar=sidebar)

# @app.route('/byactivity/<act>')
# def viewActivity(act):
#     if act=="../":
#         return redirect(url_for('index'))
#     # else:
#     return render_template('byactivity.html')