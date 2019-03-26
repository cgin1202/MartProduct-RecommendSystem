from pydb import dbconnection

def count():
    conn = dbconnection()
    curs = conn.cursor()
    sql="SELECT COUNT(id) FROM client"
    abc=curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        print(row[0])

    conn.close()
