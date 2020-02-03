import os
import pandas as pd

caminho_arquivo = "caminho"
count = 0
list = []

for arquivo in os.listdir(caminho_arquivo):

    file = open(caminho_arquivo + "/" + arquivo, 'r')
    
    for linha in file:
        #Separador dos campos
        campos = linha.split("|")

        campo = campos[0]

        columns = ['nome das colunas']
        
        list.append([campo])

    file.close()
    dataframe_arquivo = pd.DataFrame(list, columns=columns)
    arquivo_especifico = dataframe_arquivo[dataframe_dump['coluna_arquivo'].str.match('o_que_precisa_ser_procurado')]

    print (arquivo_especifico)
    arquivo_especifico.to_csv(r'Caminho a ser salvo'+ arquivo, index=None, sep=';', mode='a')
    list = []

