import sqlite3

class Database:
    """docstring for Database."""

    def __init__(self, databasename):
        self.databasename = databasename
        self.conn = sqlite3.connect(databasename)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER, name TEXT, number INTEGER, balance REAL)")
        self.conn.commit()


    def insert(self, id, name, number, balance):
        self.cursor.execute("INSERT INTO accounts VALUES(?,?,?,?)", (id,name,number,balance))
        self.conn.commit()

    def views(self):
        self.cursor.execute("SELECT * FROM accounts")
        rows = self.cursor.fetchall()
        return rows


    def __del__(self):
        self.conn.close()


connect = Database("accouts.db")
connect.insert(4, 'Hilali Hassani', 120334920324, 4000)
print(connect.views())
