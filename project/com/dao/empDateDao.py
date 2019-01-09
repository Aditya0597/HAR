from project.com.dao import conn_db

conn=conn_db()

class byDate:
    def empByDate(self,date):
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM employee WHERE date={}'.format(date))
        data=cursor.fetchall()
        return data