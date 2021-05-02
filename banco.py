import mysql.connector

class Banco:

    def __init__(self):

        self.connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            port = '3306'
        )
        
        self.cursor = self.connect.cursor() 

    
    def inserir_usuario(self, usuario):
        query = f"""
            INSERT INTO Usuario VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(query, usuario)


    def inserir_usuarios(self, usuarios):
        for usuario in usuarios:
            self.inserir_usuario(usuario)

    

    def update_usuario(self, id, dados):
        query = f"""
            SELECT * FROM Usuario WHERE id = {id}
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if(result):
            query = f"""
            UPDATE Usuario SET nome={dados['nome']}, cpf={dados['cpf']}, email={dados['email']} WHERE id = {id}
            """
            self.cursor.execute(query)
    

    def delete_usuario(self, id):
        query = f"""
            DELETE FROM Usuario WHERE id = {id}
        """
        self.cursor.execute(query)


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
