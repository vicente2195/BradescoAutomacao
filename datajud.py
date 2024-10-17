#API Datajud
#Documentação completa: https://datajud-wiki.cnj.jus.br/
#Glossário de Dados: https://datajud-wiki.cnj.jus.br/api-publica/glossario

import requests
import json
import credenciais
import regua_tribunal_url

def pesquisar_classe_processual_orgao_julgador(classeProcessual, orgaoJulgador):
    #classeProcessual Formato --> 1116
    #orgaoJulgador Formato --> 13597

    url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search"

    payload = json.dumps({
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {"match": {"classe.codigo": classeProcessual}},
                    {"match": {"orgaoJulgador.codigo": orgaoJulgador}}
                ]
            }
        },
        "sort": [{"dataAjuizamento": {"order": "desc"}}]
    }
    )


    headers = {
      'Authorization': credenciais.APIKey,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def obter_url_por_tribunal(nomeTribunal):
    for tribunal in regua_tribunal_url.regua_tribunal:
        if tribunal['tribunal'] == nomeTribunal:
            return tribunal['url']
    return None  # Retorna None se o tribunal não for encontrado

def pesquisar_numero_processo(numeroProcesso, nomeTribunal):
    #numeroProcesso Formato --> 15084471220228260266

    url = obter_url_por_tribunal(nomeTribunal)

    payload = json.dumps({
        "query": {
            "match": {
                "numeroProcesso": numeroProcesso
            }
        }
    })


    headers = {
        'Authorization': credenciais.APIKey,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

