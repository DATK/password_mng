# imports
from src.shifrs import Shifer
import sqlite3 as sq

# shifrs
sh = Shifer()

# sqlSHABL

sql1 = "INSERT INTO users (Name, Password) VALUES (?,?);"
sql2 = "SELECT * FROM users WHERE Name==?;"
sql3 = "INSERT INTO data (Name, Password) VALUES (?,?);"
sql4 = "DELETE FROM data WHERE Name==? and Password==?;"
sql5 = "SELECT * FROM data;"
sql6 = "DELETE FROM data;"
# FUNCS


# classes
class User:

    def __init__(self, name: str, ps: str):
        self.connection = sq.connect('./sql/USERS_DATABASE.db')
        self.cursor = self.connection.cursor()
        self.name = name
        self.ps = sh.hashing(ps)

    def auth(self):
        try:
            self.cursor.execute(sql2, (self.name))
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

    def __init__(self):
        self.connection = sq.connect(
            './sql/manager.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.name = ""
        self.passworsd = ""

    def save(self):
        self.cursor.execute(sql3, (self.name, self.password))
        self.connection.commit()

    def set(self, name, password):
        self.password = sh.cezar(password, 4)
        self.name = name

    def del_dt(self):
        self.cursor.execute(sql4, (self.name, self.password))
        self.connection.commit()

    def del_all(self):
        self.cursor.execute(sql6)
        self.connection.commit()
        
    def output(self):
        res = list()
        pas=""
        name=""
        self.cursor.execute(sql5)
        records = self.cursor.fetchall()
        for i in records:
            for j in range(len(i)):
                if j % 3 != 0:
                    if j % 2 == 0:
                        pas=sh.uncezar(i[j], 4)
                    else:
                        name=i[j]
                    if name!="" and pas!="":  
                        tmp=f"Логин - {name} Пароль - {pas}"
                        res.append(tmp)
                        name=""
                        pas=""
   
                    
        return res
