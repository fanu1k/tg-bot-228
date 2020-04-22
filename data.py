import sqlite3


class User:
    def __init__(self, id, login, exp, complited):
        self.id = id
        self.login = login
        self.exp = exp
        self.complited = complited

    def insert_name(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute('''SELECT Login FROM database''').fetchall()
        for element in result:
            if self.login in element:
                con.close()
                return "имя занято"
        else:
            cur.execute(
                '''INSERT INTO database (ID, Login, Exp, Completed) VALUES (?, ?, 0, '0/')''', (self.id, self.login))
            con.commit()
            con.close()

    def change_exp(self, num):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            '''SELECT Exp FROM database WHERE Login = ?''', self.login).fetchone()
        self.exp = int(result[0]) + num
        cur.execute('''UPDATE database SET Exp = ? WHERE Login = ?''',
                    (self.exp, self.login))
        con.commit()
        con.close()

    def change_completed(self, exer):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            '''SELECT Completed FROM database WHERE Login = ?''', self.login).fetchone()
        self.complited = str(result[0]) + str(exer) + '/'
        cur.execute('''UPDATE database SET Completed = ? WHERE Login = ?''',
                    (self.complited, self.login))
        con.commit()
        con.close()

    def get_info(self, id):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            '''SELECT * FROM database WHERE Login = ?''', self.login).fetchone()
        con.close()
        ans = [result[1], result[2], result[3].split('/')[:-1]]
        return ans
