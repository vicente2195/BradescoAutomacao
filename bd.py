#Exemplo** Inserir no banco de dados informações novas

import sqlite3
import json







# Função para inserir dados JSON no banco de dados
def inserir(conn, json_data):
    cursor = conn.cursor()

    # Carrega o JSON em um objeto Python
    data = json.loads(json_data)

    # Itera sobre o JSON e insere os dados na tabela
    for item in data:
        cursor.execute('''
            INSERT INTO tabela (id, tribunal, processo, etc)
            VALUES (?, ?, ?)
        ''', (item['id'], item['tribunal'], item['processo'], item['etc']))

    # Salva as mudanças no banco de dados
    conn.commit()


# Função principal
def inserir_bd(json_data):
    # Conexão com o banco de dados (Apenas exemplo)
    #conn = sqlite3.connect('processos.db')



    # Insere o JSON no banco de dados
    #inserir(conn, json_data)



    # Fecha a conexão
    #conn.close()

    print("Dados inseridos com sucesso!")


