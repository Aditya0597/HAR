from flask import *
from project import app
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = LoginVO()
    log = LoginDAO()
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.password = request.form.get('password')
        print(user.username)
        print(user.password)
        data = log.login(user)
        print(data)
        if len(data) > 0:
            if data[0][-1] == user.password:
                return redirect(url_for('home'))
            return render_template('login.html', error='Password incorrect!')
        else:
            return render_template('login.html', error='Username or Password incorrect!')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('login.html')
