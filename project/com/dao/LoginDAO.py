from project.com.dao import conn_db

conn = conn_db()


class LoginDAO:
    def login(self, user):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurants WHERE name='{}'".format(user.username))
        data = cursor.fetchall()
        print(data)
        conn.commit()
        cursor.close()
        # conn.close()

        return data
