debug = 0
port = 6070
host="0.0.0.0"
ip="192.168.1.104"


sql1 = "INSERT INTO users (Name, Password) VALUES (?,?);"
sql2 = "SELECT * FROM users WHERE Name==?;"
sql3 = "INSERT INTO data (Name, Password) VALUES (?,?);"
sql4 = "DELETE FROM data WHERE Name==? and Password==?;"
sql5 = "SELECT * FROM data;"
sql6 = "DELETE FROM data;"
sql7 = 'CREATE TABLE "data" ( "ID" INTEGER NOT NULL, "Name" TEXT NOT NULL, "Password" TEXT NOT NULL, PRIMARY KEY("ID" AUTOINCREMENT) )'
sql8 = 'CREATE TABLE "users" ( "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "Name" TEXT NOT NULL, "Password" TEXT NOT NULL )'
