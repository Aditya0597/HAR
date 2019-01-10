from flask import *
from project import app
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.RegisterDAO import RegisterDAO


@app.route('/register', methods=['GET', 'POST'])
def register():
    user = RegisterVO()
    reg = RegisterDAO()
    if request.method == 'POST':
        user.email = request.form.get('email')
        user.address = request.form.get('address')
        user.name = request.form.get('name')
        user.password = request.form.get('password')

        resp = reg.register(user)

        if resp == True:
            return render_template('login.html')
        else:
            return 'error'

    else:
        return render_template('register.html')
