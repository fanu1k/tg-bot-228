import sqlite3


class User:
    def __init__(self, id, login, exp, complited):
        self.id = id
        self.login = login
        self.exp = exp
        self.complited = complited

    def get_id(self, login, flag):
        if flag is True:
            login = self.login
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT ID FROM database WHERE login = '%s'" % login).fetchone()
        con.close()
        return result

    def get_login(self, id, flag):
        if flag is True:
            id = self.id
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Login FROM database WHERE ID = '%s'" % id).fetchone()
        con.close()
        return result

    def get_exp(self, login, flag):
        if flag is True:
            login = self.login
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Exp FROM database WHERE login = '%s'" % login).fetchone()
        con.close()
        return result

    def get_complited(self, login, flag):
        if flag is True:
            login = self.login
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT Complited FROM database WHERE login = '%s'" % login).fetchone()
        con.close()
        return result

    def change_exp(self, amount, flag):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        self.exp = self.exp + amount
        cur.execute("UPDATE database SET Exp = '%s' WHERE ID = '%s'" %
                    (self.exp, self.login))
        con.commit()
        con.close()

    def change_complited(self, stage, flag):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        self.complited = self.complited + stage + '/'
        cur.execute("UPDATE database SET Exp = '%s' WHERE ID = '%s'" %
                    (stage, self.login))
        con.commit()
        con.close()

    def set_info(self):
        self.exp = 0
        self.complited = '0'
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        cur.execute("UPDATE database SET Exp = '%s', Complited = '%s' WHERE Login = '%s'" %
                    (self.exp, self.complited, self.login))
        con.commit()
        con.close()

    def get_info(self):
        con = sqlite3.connect('user_database.db')
        cur = con.cursor()
        result = cur.execute(
            "SELECT ID, Login, Exp, Complited FROM database WHERE login = '%s'" % self.login).fetchone()
        con.close()
        return result

    def update_info(self, id, login, exp, complited):
        self.id = id
        self.login = login
        self.exp = exp
        self.complited = complited
