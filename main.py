import xmltodict  # Transform XML files into dictionaries
import os  # Handle files
import json  # Convert the file to JSON for easier visualization
import pandas  # Data manipulation and analysis

def get_info(file_name, values):
    with open(f"nfs/{file_name}", "rb") as xml_file:
        dict_file = xmltodict.parse(xml_file)
        
        if "NFe" in dict_file:
            nf_info = dict_file["NFe"]["infNFe"]
        else:
            nf_info = dict_file["nfeProc"]["NFe"]["infNFe"]
        
        note_number = nf_info["@Id"]
        issuing_company = nf_info["emit"]['xNome']
        customer_name = nf_info["dest"]["xNome"]
        address = nf_info["dest"]["enderDest"]
        
        if "vol" in nf_info["transp"]:
            gross_weight = nf_info["transp"]["vol"]["pesoB"]
        else:
            gross_weight = "Not informed"

        values.append([note_number, issuing_company, customer_name, address, gross_weight])

def main():
    file_list = os.listdir('nfs')

    columns = ["note_number", "issuing_company", "customer_name", "address", "gross_weight"]

    data_values = []

    for file in file_list:
        get_info(file, data_values)

    table = pandas.DataFrame(columns=columns, data=data_values)
    table.to_excel("NFes.xlsx", index=False)

main()
