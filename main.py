import xmltodict # Transformar arquivos .xml em dicionários
import os   # Manusear arquivos

def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml: #usa-se o 'rb' para que não leia em string e sim em bytes object
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(dic_arquivo)


lista_arquivos = os.listdir('nfs') # Listar os arquivos da pasta nfs

for arquivo in lista_arquivos:
    pegar_infos(arquivo)

