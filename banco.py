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
       
        query = "INSERT INTO Usuario(nome, email, cpf, profile) VALUES (%s, %s, %s, %s)"
        
        print("sql: "+query)
        self.cursor.execute(query, user)
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

    def updateChip(self, chip, value):
        query = f"""
            UPDATE Chip SET disponivel = {value} WHERE id = {chip[0]}
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
            DELETE FROM Numero WHERE id = {id}
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

    



    def getAllPlans(self):
        query = f"""
        SELECT * FROM Plano
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()


    def getAgency(self, id):
        query = f"""
        SELECT * FROM Agencia WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()

    
    def getPlan(self, id):
        query = f"""
        SELECT * FROM Plano WHERE id = {id}
        """
        self.cursor.execute(query)

        return self.cursor.fetchone()


    def getAllAgencies(self):
        query = f"""
        SELECT * FROM Agencia
        """
        self.cursor.execute(query)

        return self.cursor.fetchall()
            

    def createNewPlan(self, plan):
        query = f"""
            INSERT INTO Plano(agencia_id, nome, preco, pagamento_id, dt_expiracao) VALUES ('{plan[0]}', '{plan[1]}', '{plan[2]}', '{plan[3]}', '{plan[4]}')
        """
        print("sql create plan: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True
    
    def updatePlan(self, plan):
        query = f"""
            UPDATE Plano SET agencia_id = '{plan[1]}', nome = '{plan[2]}', preco = '{plan[3]}', pagamento_id = '{plan[4]}', dt_expiracao = '{plan[5]}' WHERE id = {plan[0]}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True

    def deletePlan(self, id):
        query = f"""
            DELETE FROM Plano WHERE id = {id}
        """
        print("sql: "+query)
        self.cursor.execute(query)
        self.connect.commit()
        return True







# banco = Banco()
# usuario = ("askdjhasd", "ASdasd", "asdasd", "sdasd")
# banco.inserir_usuario(usuario)
