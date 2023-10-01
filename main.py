import xmltodict # Transformar arquivos .xml em dicionários
import os   # Manusear arquivos
import json


def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml: #usa-se o 'rb' para que não leia em string e sim em bytes object
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(json.dumps(dic_arquivo, indent=4))


lista_arquivos = os.listdir('nfs') # Listar os arquivos da pasta nfs

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    break

