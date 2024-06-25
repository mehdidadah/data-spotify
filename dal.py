import pymysql as my


def getconnection():
    cnx = None
    try:
        cnx = my.connect(user="root", host="127.0.0.1", port=3306, database="db_spotify")
    except my.Error as e:
        print(e)
    return cnx


def insert(records):
    cnx = getconnection()
    if cnx:
        try:
            db = cnx.cursor()
            db.execute("DELETE FROM db_spotify")
            db.executemany("INSERT INTO db_spotify VALUES(%s, %s, %s, %s, %s)", records)
            cnx.commit()
        except my.Error as e:
            print(e)
            cnx.rollback()
