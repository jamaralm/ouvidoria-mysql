from db import Database
import time

queries = {
    'select_manifestation': 'SELECT * FROM Manifestations',
    'insert_manifestation': 'INSERT INTO Manifestations (type_id, user_id, name, description) VALUES (%s, %s, %s, %s)',
    'select_type': 'SELECT name FROM ManifestTypes WHERE id = %s',
    'select_user': 'SELECT name FROM Users WHERE id = %s',
    'select_manifestation_by_type': 'SELECT * FROM Manifestations WHERE type_id = %s',
    'count_manifestations': 'SELECT COUNT(*) as count_Manifestation FROM Manifestations;',
    'delete_manifestation': 'DELETE FROM Manifestations WHERE id=%s;',
    'select_manifestation_by_id': 'SELECT * FROM Manifestations WHERE id = %s'
}

db = Database('localhost', 'root', '12345', 'Projeto_Ouvidoria')
options = ['Listar Manifestacoes', 'Listar Manifestacoes por Tipo', 'Adicionar Manifestacao', 'Contar Manifestações', 'Selecionar Manifestacao Por Id', 'Apagar Manifestacao', 'Sair']
manifestation_types = ['Reclamacao', 'Sugestao', 'Elogio', 'Denuncia', 'Duvida']


def option_menu(option_list):
    for index, option in enumerate(option_list):
        print(f'{index+1}. {option}')

def add_manifestation(type, user, name, description):
    db.executar_query(queries['insert_manifestation'], (type, user, name, description))


def list_manifestations():
    list_manifestations = db.executar_query(queries['select_manifestation'], fetch=True)

    print(f'{"ID"} | {"TITULO":<25} | {"TIPO":<12} | {"USUARIO":<10}')
    print('-' * 60)

    for manifestation in list_manifestations:
        manifestation_type = db.executar_query(queries['select_type'], (manifestation[1],), fetch=True)
        manifestation_type = manifestation_type[0][0]

        manifestation_user = db.executar_query(queries['select_user'], (manifestation[2],), fetch=True)
        manifestation_user = manifestation_user[0][0]

        print(f'{manifestation[0]:<2} | {manifestation[3]:<25} | {manifestation_type:<12} | {manifestation_user:<10}')


def list_manifestations_by_type(type_id):
    manifestation_list = db.executar_query(queries['select_manifestation_by_type'], (type_id,), fetch=True)
    manifestation_type = db.executar_query(queries['select_type'], (type_id,), fetch=True)

    print('\n')
    print('-' * 71)
    print(f'CATEGORIA: {manifestation_type[0][0]:<58} |')
    print('-' * 71)

    for manifestation in manifestation_list:
        print(f'{manifestation[0]} | {manifestation[4]:<65} |')

    print('-' * 71)

def count_manifestations():
    manifestation_quantity = db.executar_query(query=queries['count_manifestations'], fetch=True)

    print('\n')
    print(f'QUANTIDADE DE MANIFESTACOES: {manifestation_quantity[0][0]}') 

def delete_manifestation(manifestation_id):
    db.executar_query(query=queries['delete_manifestation'])

    print(f'Manifestacao {manifestation_id} Deletada com sucesso!')

def select_manifestation(manifestation_id):
    manifestation = db.executar_query(
        query=queries['select_manifestation_by_id'], 
        parametros=(manifestation_id,), 
        fetch=True
    )

    if not manifestation:
        print("Manifestação não encontrada.")
        return

    manifestation_data = manifestation[0]  # Pegamos a primeira (e única) ocorrência
    user = db.executar_query(queries['select_user'], (manifestation_data[2],), fetch=True)
    type = db.executar_query(queries['select_type'], (manifestation_data[1],), fetch=True)

    user_name = user[0][0] if user else "Desconhecido"
    type_name = type[0][0] if type else "Desconhecido"

    print("\n" + "-" * 80)
    print(f"{'DETALHES DA MANIFESTAÇÃO':^80}")
    print("-" * 80)
    print(f" ID: {manifestation_data[0]}")
    print(f" Tipo: {type_name}")
    print(f" Usuário: {user_name}")
    print(f" Título: {manifestation_data[3]}")
    print(f" Descrição:\n {manifestation_data[4]}")
    print(f" Data: {manifestation_data[5].strftime('%d/%m/%Y')}")
    print(f" Status: {'Aberto' if manifestation_data[6] == 0 else 'Fechado'}")
    print("-" * 80)

'''
    MAIN CODE
'''

def main():
    while True:
        print("\nOPCOES: ")
        option_menu(options)

        user_choice = int(input('\nESCOLHA UMA OPCAO: '))

        # LISTAR MANIFESTACAO
        if user_choice == 1:
            list_manifestations()

        # LISTAR MANIFESTACAO POR TIPO
        elif user_choice == 2:
            print("-" * 22)
            print('TIPOS DE MANIFESTACAO')
            print("-" * 22)
            option_menu(manifestation_types)

            user_type_choice = int(input("ESCOLHA UM TIPO: "))
            list_manifestations_by_type(user_type_choice)

        # ADICIONAR MANIFESTACAO
        elif user_choice == 3:
            print("-" * 22)
            print('TIPOS DE MANIFESTACAO')
            print("-" * 22)
            option_menu(manifestation_types)

            user_type_choice = int(input("ESCOLHA UM TIPO: "))
            user_id_input = int(input("DIGITE O ID DO USER: "))
            manifestation_name = input("NOME DA MANIFESTACAO: ")
            manifestation_description = input("DIGITE A DESCRICAO: ")

            add_manifestation(user_type_choice, user_id_input, manifestation_name, manifestation_description)

        #CONTAR MANIFESTACOES
        elif user_choice == 4:
            count_manifestations()
        
        elif user_choice == 5:
            manifestation_id = int(input('DIGITE O ID DA MANIFESTACAO: '))
            select_manifestation(manifestation_id=manifestation_id)

        #APAGAR MANIFESTACOES
        elif user_choice == 6:
            manifestation_id_input = int(input('ID DA MANIFESTACAO QUE DESEJA APAGAR: '))
            delete_manifestation(manifestation_id=manifestation_id_input)
        
        #TERMINAR EXECUCAO
        elif user_choice == 7:
            print('SAINDO...')
            time.sleep(1.5)
            break

if __name__ == '__main__':
    main()

db.fechar_conexao()