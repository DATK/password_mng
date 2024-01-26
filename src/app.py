# imports
from src.shifrs import Shifer
import sqlite3 as sq
from src.config import sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8
# shifrs
sh = Shifer()


# classes
class User:

    def __init__(self, name: str, ps: str):
        self.connection = sq.connect('./sql/USERS_DATABASE.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.name = name
        self.ps = sh.hashing(ps)
        self.create_db()
        
    def create_db(self):
        try:
            self.cursor.execute(sql8)
            self.connection.commit()
        except sq.OperationalError:
            return 1

    def auth(self):
        try:
            self.cursor.execute(sql2, (self.name,))
            records = self.cursor.fetchall()
            for i in records:
                if i[1] == self.name and i[2] == self.ps:
                    return 1
                else:
                    return 1
        except:
            return 0

    def reg(self):
        self.cursor.execute(sql1, (self.name, self.ps))
        self.connection.commit()
        return 1

    def get(self):
        return (self.name, self.ps)

    def __del__(self):
        self.connection.close()


class Manager:

    def __init__(self, db, user: object):
        self.user = user
        self.name = ""
        self.passworsd = ""
        self.connection = sq.connect(
            f'./sql/{db}.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def save(self):
        self.cursor.execute(sql3, (self.name, self.password))
        self.connection.commit()

    def set(self, name, password):
        self.password = sh.cezar(password, 4)
        self.name = name

    def chek_usr_auth(self, nm):
        if self.user.get()[0] == nm and self.user.auth():
            return True
        else:
            return False

    def create_table(self):
        try:
            self.cursor.execute(sql7)
            self.connection.commit()
        except sq.OperationalError:
            return 1

    def del_dt(self):
        self.cursor.execute(sql4, (self.name, self.password))
        self.connection.commit()

    def del_all(self):
        self.cursor.execute(sql6)
        self.connection.commit()

    def output(self):
        res = list()
        pas = ""
        name = ""
        self.cursor.execute(sql5)
        records = self.cursor.fetchall()
        for i in records:
            for j in range(len(i)):
                if j % 3 != 0:
                    if j % 2 == 0:
                        pas = sh.uncezar(i[j], 4)
                    else:
                        name = i[j]
                    if name != "" and pas != "":
                        tmp = f"Логин - {name} Пароль - {pas}"
                        res.append(tmp)
                        name = ""
                        pas = ""

        return res

    def __del__(self):
        self.connection.close()
