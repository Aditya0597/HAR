from project.com.dao import conn_db

conn = conn_db()


class dashboard:
    def empByActivity(self, act):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE activity='{}'".format(act))
        data = cursor.fetchall()
        return data

    def empBySession(self, session_time):
        cursor = conn.cursor()
        print(session_time)
        cursor.execute("SELECT * FROM employees WHERE session_time='{}'".format(session_time))
        data = cursor.fetchall()
        return data

    def empByArea(self, area):
        cursor = conn.cursor()
        print(area)
        cursor.execute("SELECT * FROM employees WHERE area='{}'".format(area))
        data = cursor.fetchall()
        return data
