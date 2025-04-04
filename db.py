import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        """Inicializa a conexão com o banco de dados."""
        self.connection = self._criar_conexao(host, user, password, database)

    def _criar_conexao(self, host, user, password, database):
        """Cria uma conexão com o banco de dados."""
        try:
            return mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    def fechar_conexao(self):
        """Encerra a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()

    def executar_query(self, query, parametros=None, fetch=False):
        """
        Executa uma query no banco de dados.
        
        - `query`: Comando SQL a ser executado.
        - `parametros`: Tupla com valores para a query.
        - `fetch`: Se True, retorna os resultados da consulta.
        """
        if not self.connection:
            print("Conexão com o banco de dados não estabelecida.")
            return None if fetch else 0

        try:
            cursor = self.connection.cursor(prepared=True)
            cursor.execute(query, parametros or ())
            
            if fetch:
                resultado = cursor.fetchall()
            else:
                self.connection.commit()
                resultado = cursor.lastrowid if "INSERT" in query.upper() else cursor.rowcount

        except Error as err:
            print(f"Erro ao executar a query: {err}")
            self.connection.rollback()
            return None if fetch else 0

        finally:
            cursor.close()

        return resultado