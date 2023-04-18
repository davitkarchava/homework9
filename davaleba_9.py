import sqlite3


def db_connection(file):
    return sqlite3.connect(file)


def select_all(conn):
    print("---SELECT ALL DATA FROM USERS---")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users")
    for row in result:
        print(row)


def moqmedeba_1(conn):
    print("---SELECT USERNAME AND PHONE_NAMBER FROM USERS---")
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row[1])
        print(row[5])


def moqmedeba_2(conn):
    print("---SELECT FIRSTNAME LASTNAME AND AGE FROM USERS WHERE AGE > 25---")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE age > 25")
    for row in result:
        print(row[2])
        print(row[3])
        print(row[4], "წლის")


def moqmedeba2(conn):
    print("---SELECT FIRSTNAME LASTNAME AND AGE FROM USERS WHERE AGE > 25---")
    """გამოვიყენე ცვლადი"""
    age = 25
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE age > ?", (age,))
    for row in result:
        print(row[2])
        print(row[3])
        print(row[4], "წლის")


def moqmedeba_3(conn):
    print("---SELECT ALL DATA FROM USERS WHERE AGE IS BETWEEN 10 AND 25---")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
    for row in result:
        print(row)


def moqmedeba_4(conn):
    print("---SELECT FIRSTNAME LASTNAME FROM USERS WHERE AGE <> 20---")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE age <> 20")
    for row in result:
        print(row[2], row[3])


def moqmedeba_5(conn):
    print("---RECORD COUNT--")
    cursor = conn.cursor()
    count = cursor.execute("SELECT COUNT( * ) FROM users")
    for i in count:
        print(i)


def moqmedeba_6(conn):
    print("---SELECT ALL DATA FROM USERS ACCORDING TO DECREASING AGE---")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users ORDER BY age desc")
    for row in result:
        print(row)


def moqmedeba_7(conn):
    print("---SELECT DISTINCT FIRSTNAME ACCRDING TO INCREASING---")
    """მემგონი ანბანის მიხედვით უნდოდა აქ :)"""
    cursor = conn.cursor()
    result = cursor.execute("SELECT DISTINCT firstname FROM users ORDER BY firstname ")
    for row in result:
        print(row)


def moqmedeba_8(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = 'dachi' WHERE age = 20 ")
    conn.commit()


def moqmedeba_9(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = 15 WHERE age = 30")
    conn.commit()


def moqmedeba_10(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = 5")
    conn.commit()


def moqmedeba_11(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE SUBSTRING(firstname, 1, 1) = 'ა'")
    conn.commit()


def main():
    conn = db_connection("customers.sqlite")
    select_all(conn)
    moqmedeba_1(conn)
    moqmedeba_2(conn)
    moqmedeba2(conn)
    moqmedeba_3(conn)
    moqmedeba_4(conn)
    moqmedeba_5(conn)
    moqmedeba_6(conn)
    moqmedeba_7(conn)
    moqmedeba_8(conn)
    moqmedeba_9(conn)
    moqmedeba_10(conn)
    moqmedeba_11(conn)
    conn.close()


main()
