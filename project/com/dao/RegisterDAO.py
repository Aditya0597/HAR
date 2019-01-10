from project.com.dao import conn_db

conn = conn_db()


class RegisterDAO:
    def register(self, user):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO restaurants ('email','address','name','password') values('{}','{}','{}','{}');".format(
                user.email, user.address, user.name, user.password))
        conn.commit()
        cursor.close()
        # conn.close()

        return True
