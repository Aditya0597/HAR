from project.com.dao import conn_db

conn=conn_db()

class byActivity:
    def empByActivity(self,act):
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM employee WHERE activity={}'.format(act))
        data=cursor.fetchall()
        return data