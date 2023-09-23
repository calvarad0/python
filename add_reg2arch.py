#from random import randint as rnd
import random

def genData(df,registros):
    with open(df,'r+') as file:
        totLines = len(file.readlines())
        print(f"incio registros:{totLines-1}")

        for i in range(totLines,registros+1):
            a = random.choice(tipo)
            b = random.randint(0,25)
            #print(f"CAMPO-{i};DATAELEM-{i};{a};{b};0;Descripción-{i}")
            file.write(f"\nCAMPO-{i};DATAELE-{i};{a};{b};0;Descripción-{i}")

        print(f"Finalizo - registros:{i}")

def genData2(df,registros):
    with open(df,'r+') as file:
        totLines = len(file.readlines())
        print(f"incio registros:{totLines-1}")

        for i in range(totLines,registros+1):
            a = random.choice(tipo)
            b = random.randint(0,25)
            #print(f"CAMPO-{i};DATAELEM-{i};{a};{b};0;Descripción-{i}")
            file.write(f"\nCAMPO-{i};DATAELE-{i};{a};{b};0;Descripción-{i}")

        print(f"Finalizo - registros:{i}")


nRegistros = 100000

#Campo;Elemento de Datos;Tipo;Long;Dec;Descripción Breve
tipo = ("CLNT","CHAR","NUMC","DATS","TIMS")
csvData = "zptmx085.csv"

genData(csvData,nRegistros)

cfdiArchivos = "CFDI_ARCHIVOS.csv"

genData2(cfdiArchivos,nRegistros)
