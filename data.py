import sqlite3


<<<<<<< Updated upstream
def insert_name(num, string):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT Name FROM database''').fetchall()
    for element in result:
        if string in element:
            con.close()
            return "имя занято"
    else:
        cur.execute(
            '''INSERT INTO database (ID, Name, Exp, Completed) VALUES (?, ?, 0, '0/')''', (num, string))
=======
def insert_name(id, name):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT Name FROM database''').fetchall()
    if name in result:
        con.close()
        return "имя занято"
    else:
        cur.execute('''INSERT INTO database(ID, Name, Exp, Completed) VALUES(id, name, 0, 0)''')
>>>>>>> Stashed changes
        con.commit()
        con.close()


def change_exp(id, num):
<<<<<<< Updated upstream
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT Exp FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Exp = ? WHERE ID = ?''',
                (int(result[0]) + num, id))
=======
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT Exp FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Exp = ? WHERE ID = ?''', (int(result[0]) + num, id))
>>>>>>> Stashed changes
    con.commit()
    con.close()


def change_completed(id, exer):
<<<<<<< Updated upstream
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT Completed FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Completed = ? WHERE ID = ?''',
                (str(result[0]) + str(exer) + '/', id))
=======
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT Completed FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Completed = ? WHERE ID = ?''', (str(result[0]) + str(exer), id))
>>>>>>> Stashed changes
    con.commit()
    con.close()


def get_info(id):
<<<<<<< Updated upstream
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT * FROM database WHERE ID = ?''', (id,)).fetchone()
    con.close()
    ans = [result[1], result[2], result[3].split('/')[:-1]]
    return ans
=======
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT * FROM database WHERE ID = ?''', (id,)).fetchone()
    con.close()
    return result
>>>>>>> Stashed changes
