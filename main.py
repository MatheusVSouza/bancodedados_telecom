import mysql.connector




cursor = db.cursor()
cursor.execute("use TelecomDB;")

usuario = ("akjhds", "aksdh", "asdasd")

# SET DATA
query = f"""
    INSERT INTO Usuario(id, nome, cpf, email) VALUES (2, "Paulo", "819981273", "paulo@email.com");
"""
cursor.execute(query)
db.commit()

 

# GET OUTPUT
query = f"""
    SELECT * FROM Usuario;
"""
cursor.execute(query)
output = cursor.fetchall()
print(output)



def exec_query(self, query):
    self.cursor.execute(query)

 
