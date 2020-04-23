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
                    (self.exp, self.login))
        con.commit()
        con.close()

    def change_completed(self, exer):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        self.complited = '/' + str(exer) + '/'
        cur.execute("UPDATE database SET Completed = '%s' WHERE Login = '%s'" %
                    (self.complited, self.login))
        con.commit()
        con.close()

    def get_info(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT * FROM database WHERE Login = '%s'" % self.login).fetchone()
        con.close()
        ans = [result[1], result[2], result[3]]
        return ans

    def get_login(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Login FROM database WHERE ID = '%s'" % self.id).fetchone()
        con.close()
        print(result)
        return result[0]

    def get_exp(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Exp FROM database WHERE Login = '%s'" % self.login).fetchone()
        con.close()
        return result[0]

    def get_id(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT ID FROM database WHERE Login = '%s'" % self.login).fetchone()
        con.close()
        return result[0]

    def set_info(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        cur.execute(" UPDATE database SET Exp = '%s', Complited = '%s' WHERE Login = '%s'" %
                    (0, 0, self.get_login()))
        con.commit()
        con.close()
