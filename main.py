import xmltodict # Transformar arquivos .xml em dicionários
import os   # Manusear arquivos
import json #Converter o arquivo em JSON para facilitar a visualização
import pandas

def pegar_infos(nome_arquivo, valores):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml: #usa-se o 'rb' para que não leia em string e sim em bytes object
          
            dic_arquivo = xmltodict.parse(arquivo_xml)
            print(json.dumps(dic_arquivo, indent=4))
            
            if "NFe" in dic_arquivo:
                infos_nf = dic_arquivo["NFe"]["infNFe"]
            else:
                infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
            numero_nota = infos_nf["@Id"]
            empresa_emissora = infos_nf["emit"]['xNome']
            nome_cliente = infos_nf["dest"]["xNome"]
            endereco = infos_nf["dest"]["enderDest"]
            
            if "vol" in infos_nf["transp"]:
                peso_bruto = infos_nf["transp"]["vol"]["pesoB"]
            else:
                peso_bruto = "Não informado"

            valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso_bruto])

lista_arquivos = os.listdir('nfs') # Listar os arquivos da pasta nfs

colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso_bruto"]

valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

tabela = pandas.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False) 
