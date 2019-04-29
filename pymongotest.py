from pymongodb import dbconnection

conn = dbconnection()
db = conn.admin
print(db)