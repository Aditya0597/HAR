from project.com.dao import conn_db

conn=conn_db()

class dashboard:
    def empByActivity(self,act):
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE activity='{}'".format(act))
        data=cursor.fetchall()
        return data