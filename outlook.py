import re
import win32com.client
import credenciais

import win32com.client
import re

def verificar_email_novo():
    # Conexão com o Outlook
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    # Acessa a pasta "Bradesco"
    bradesco_folder = None
    for folder in outlook.Folders:
        if folder.Name == credenciais.UsuarioOutlook:  # Altere para o seu nome de usuário do Outlook
            for subfolder in folder.Folders:
                if subfolder.Name == "Bradesco":
                    bradesco_folder = subfolder
                    break

    if not bradesco_folder:
        print("Pasta 'Bradesco' não encontrada.")
        return []

    # Filtra emails não lidos
    messages = bradesco_folder.Items
    unread_messages = messages.Restrict("[Unread] = True")

    # Converte a coleção de mensagens não lidas em uma lista
    unread_messages_list = list(unread_messages)

    # Define o padrão de regex para extrair informações do assunto
    pattern = r"PROCESSO BRADESCO - (.*?) - (\d+)"

    # Lista para armazenar os tribunais e processos encontrados
    lista_tribunais_processos = []

    # Percorre os emails não lidos
    for message in unread_messages_list:
        match = re.search(pattern, message.Subject)
        if match:
            tribunal = match.group(1)  # Nome do tribunal
            numero_processo = match.group(2)  # Número do processo

            # Adiciona o tribunal e o número do processo à lista
            lista_tribunais_processos.append({
                "tribunal": tribunal,
                "numero_processo": numero_processo
            })

            # Marca o email como lido
            message.Unread = False
            message.Save()

    # Retorna a lista de tribunais e processos
    return lista_tribunais_processos








def enviar_email_outlook(lista_processos):
    # Cria uma instância do Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 = olMailItem

    # Configura o e-mail
    mail.Subject = 'Processos inseridos no banco de dados com sucesso!'
    mail.To = credenciais.DestinatarioOutlook  # Substitua pelo e-mail de destino

    # Monta o corpo do e-mail
    mensagem = 'Os seguintes processos foram inseridos no banco de dados com sucesso:\n\n'
    for item in lista_processos:
        tribunal = item['tribunal']
        numero_processo = item['numero_processo']
        mensagem += f'Tribunal: {tribunal}, Número do processo: {numero_processo}\n'

    # Adiciona a mensagem ao corpo do e-mail
    mail.Body = mensagem

    # Envia o e-mail
    mail.Send()

    print("E-mail enviado com sucesso.")





