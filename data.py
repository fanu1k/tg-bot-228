import sqlite3


class User:
    def __init__(self, id, login, exp, complited):
        self.id = id
        self.login = login
        self.exp = exp
        self.complited = complited

    def change_exp(self, num):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Exp FROM database WHERE Login = '%s'" % self.login).fetchone()
        self.exp = result[0] + num
        cur.execute(" UPDATE database SET Exp = '%s' WHERE Login = '%s'" %
                    (self.exp, self.login)).fetchone()
        con.commit()
        con.close()

    def change_completed(self, exer):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Completed FROM database WHERE Login = '%s'" % self.login).fetchone()
        self.complited = '/' + str(exer) + '/'
        cur.execute("UPDATE database SET Completed = '%s' WHERE Login = '%s'" %
                    (self.complited, self.login)).fetchone()
        con.commit()
        con.close()

    def get_info(self, id):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT * FROM database WHERE Login = '%s'" % self.login).fetchone()
        con.close()
        ans = [result[1], result[2], result[3]]
        return ans
