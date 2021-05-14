import mysql.connector

class Banco:

    def __init__(self):

        self.connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            port = '3306'
        )
        
        query = f"""
        USE TelecomDB
        """
        
        self.cursor = self.connect.cursor() 
        self.cursor.execute(query)

    def showMessage(self):
        print("TA FUNCIONANDO")

    def getAllUsers(self):
        query = f"""
        SELECT * FROM Usuario
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def getUser(self, id):
        query = f"""
        SELECT * FROM Usuario WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    def createNewUser(self, user):
        query = f"""
            INSERT INTO Usuario(nome, email, cpf) VALUES ('{user[0]}', '{user[1]}', '{user[2]}')
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True
    
    def updateUser(self, user):
        query = f"""
            UPDATE Usuario SET nome = '{user[1]}', email = '{user[2]}', cpf = '{user[3]}' WHERE id = {user[0]}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True

    def deleteUser(self, id):
        query = f"""
            DELETE FROM Usuario WHERE id = {id}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True

    def inserir_usuario(self, usuario):
        query = f"""
            INSERT INTO Usuario VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(query, usuario)



    def getAllNumbers(self):
        query = f"""
        SELECT * FROM Numero
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()
    def getNumber(self, id):
        query = f"""
        SELECT * FROM Numero WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    
    def getDDD(self, id):
        query = f"""
        SELECT * FROM DDD WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    def getDDI(self, id):
        query = f"""
        SELECT * FROM DDI WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()
    
    def getChip(self, id):
        query = f"""
        SELECT * FROM Chip WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    def getOperadora(self, id):
        query = f"""
        SELECT * FROM Operadora WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    def updateChip(self, chip):
        query = f"""
            UPDATE Chip SET disponivel = 0 WHERE id = {chip[0]}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True


    def createNewNumber(self, number):
        query = f"""
            INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel) VALUES ('{number[0]}', '{number[1]}', '{number[2]}', '{number[3]}', '{number[4]}', 0)
        """
        print("sql create number: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True
    
    def updateNumber(self, number):
        query = f"""
            UPDATE Numero SET user_id = '{number[1]}', ddd_id = '{number[2]}', ddi_id = '{number[3]}', chip_id = '{number[4]}', numero = '{number[5]}', disponivel = 0 WHERE id = {number[0]}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True

    def deleteNumber(self, id):
        query = f"""
            DELETE FROM Usuario WHERE id = {id}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True





    def getAllOperadoras(self):
        query = f"""
        SELECT * FROM Operadora
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()
    
    def getAllDDDs(self):
        query = f"""
        SELECT * FROM DDD
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()
    
    def getAllDDIs(self):
        query = f"""
        SELECT * FROM DDI
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def getAllChipsFromOperadora(self, id):
        query = f"""
        SELECT * FROM Chip WHERE operadora_id = {id} AND disponivel = 1
        """

        print("sql from chips: "+query)
        self.cursor.execute(query)

        return self.cursor.fetchall()

    

    def inserir_numero(self, numero):
        query = f"""
            INSERT INTO Numero VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        self.cursor.execute(query, Numero)


    def inserir_numeros(self, numeros):
        for Numero in Numeros:
            self.inserir_numero(Numero)

    

    def update_numero(self, id, dados):
        query = f"""
            SELECT * FROM Numero WHERE id = {id}
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if(result):
            query = f"""
            UPDATE Numero SET nome={dados['nome']}, cpf={dados['cpf']}, email={dados['email']} WHERE id = {id}
            """
            self.cursor.execute(query)
    

    def delete_numero(self, id):
        query = f"""
            DELETE FROM Numero WHERE id = {id}
        """
        self.cursor.execute(query)

            





# banco = Banco()
# usuario = ("askdjhasd", "ASdasd", "asdasd", "sdasd")
# banco.inserir_usuario(usuario)
