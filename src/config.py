debug=True
port=6070



sql1 = "INSERT INTO users (Name, Password) VALUES (?,?);"
sql2 = "SELECT * FROM users WHERE Name==?;"
sql3 = "INSERT INTO data (Name, Password) VALUES (?,?);"
sql4 = "DELETE FROM data WHERE Name==? and Password==?;"
sql5 = "SELECT * FROM data;"
sql6 = "DELETE FROM data;"