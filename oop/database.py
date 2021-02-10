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


    def update(self, name, number, balance, id):
        self.cursor.execute("UPDATE accounts SET name=?, number=?, balance=? WHERE id=?", (name,number,balance, id))
        self.conn.commit()


    def delete(self, id):
        self.cursor.execute("DELETE FROM accounts WHERE id=?", (id,))
        self.conn.commit()


    def __del__(self):
        self.conn.close()



class Account(Database):
    """docstring for Account."""

    def __init__(self, id, databasename):
        Database.__init__(self, databasename)
        self.databasename = databasename
        self.id  = id

    def deposit(self, amount):
        self.balance =+ amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('no enouph balance')

     def commit(self, id):
         self.cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (balance, id))
         self.conn.commit()



connect = Database("accouts.db")
connect.insert(11, 'Hilali Hassani', 120334920324, 4000)
connect.update('Hilali Hassani ABDALLA', 120334920324, 4000, 10)
connect.delete(10)

print(connect.views())
