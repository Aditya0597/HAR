from flask import *
from project import app
from project.com.dao import conn_db
from project.com.dao.dashboardDao import dashboard

@app.route('/byactivity',methods=['POST','GET'])
def viewActivity():
    if request.method=='GET':
        return render_template('byactivity.html',tables=0)
    else:
        act=request.form.get('act')
        byact=dashboard()
        data=byact.empByActivity(act)
        print(data)
        return render_template('byactivity.html',tables=1,emps=data)

# @app.route('/byactivity/<act>')
# def viewActivity(act):
#     if act=="../":
#         return redirect(url_for('index'))
#     # else:
#     return render_template('byactivity.html')