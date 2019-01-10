import sqlite3


def conn_db():
    return sqlite3.connect('har.db', check_same_thread=False)
