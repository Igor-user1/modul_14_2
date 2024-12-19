import sqlite3

con = sqlite3.connect('not_telegram.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
""")

cur.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cur.execute("INSERT INTO Users (username, email, age, balance)"
                "VALUES (?, ?, ?, ?)", (f"User{i}",f'example{i}@gmail.com', i*10, 1000))

for i in range(1, 11, 2):
    cur.execute("UPDATE Users SET balance = ? WHERE id=?", (500, i))


for i in range(1, 11, 3):
     cur.execute("DELETE FROM users WHERE id=?", (i,))

res = cur.execute("SELECT * FROM Users WHERE age <> 60")
for i in res.fetchall():
        print(f'Имя: {i[1]} | Почта: {i[2]}  | Возраст: {i[3]}  | Баланс: {i[4]} ')

cur.execute('DELETE FROM Users WHERE id=?', (6,))

res1 = cur.execute('SELECT COUNT(id) FROM Users')
print(res1.fetchone()[0])

res2 = cur.execute('SELECT SUM(balance) FROM Users')
print(res2.fetchone()[0])

res3 = cur.execute('SELECT AVG(balance) FROM Users')
print(res3.fetchone()[0])

con.commit()
con.close()
