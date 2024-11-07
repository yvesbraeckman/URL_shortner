import sqlite3
con = sqlite3.connect("experiment")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Students(FirstName, LastName)")

cur.execute("""
    INSERT INTO Students VALUES
        ('Yves', 'Braeckman'),
        ('Senne', 'De Jonge'),
        ('Kobe', 'Nevelsteen')
""")

con.commit()

res = cur.execute("SELECT FirstName FROM Students")
print(res.fetchall())

