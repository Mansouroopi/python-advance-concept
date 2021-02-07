import sqlite3


def connect():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(item, qty, price):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, qty, price))
    con.commit()
    con.close()

def views():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.close()
    return rows


def delete(item):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    con.commit()
    con.close()


def update(qty, price, item):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("UPDATE store SET qty = ?, price = ? WHERE item=?", (qty, price, item))
    con.commit()
    con.close()


# connect()
insert('android', 10, 2900)
insert('iphone', 22, 3500)
# delete("android 10")
update(100, 500, 'iphone')
print(views())
