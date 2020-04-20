import sqlite3


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
        con.commit()
        con.close()


def change_exp(id, num):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT Exp FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Exp = ? WHERE ID = ?''',
                (int(result[0]) + num, id))
    con.commit()
    con.close()


def change_completed(id, exer):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT Completed FROM database WHERE ID = ?''', (id,)).fetchone()
    cur.execute('''UPDATE database SET Completed = ? WHERE ID = ?''',
                (str(result[0]) + str(exer) + '/', id))
    con.commit()
    con.close()


def get_info(id):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT * FROM database WHERE ID = ?''', (id,)).fetchone()
    con.close()
    ans = [result[1], result[2], result[3].split('/')[:-1]]
    return ans
