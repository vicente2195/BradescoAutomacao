# Este projeto visa criar um template de automação para o Bradesco

import datajud
import outlook
import bd

def orquestrador():
    erro = ""
    try:
        # Chama a função que verifica se tem algum email novo e retorna a lista de informações novas (Tribunal e Processo)
        lista_tribunais_processos = outlook.verificar_email_novo()

        # Verifica se a lista está vazia
        if not lista_tribunais_processos:
            erro = "Nenhum email não lido encontrado com o padrão esperado."
            resultado = ""
            return erro, resultado

        # Itera sobre cada item da lista e processa os dados
        for item in lista_tribunais_processos:
            tribunal = item['tribunal']
            numero_processo = item['numero_processo']


            json = datajud.pesquisar_numero_processo(numero_processo, tribunal)
            bd.inserir_bd(json)
    except:
        erro = "Houve algum erro durante o processamento"
        resultado = ""

    if erro == "":
        outlook.enviar_email_outlook(lista_tribunais_processos)
        resultado = "Processamento finalizado com sucesso!"


    return erro, resultado




# Chamando a função principal
if __name__ == "__main__":
    erro, resultado = orquestrador()
    print(erro)
    print(resultado)