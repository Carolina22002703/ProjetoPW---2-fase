import json

def pede_nome(nome):
    if (nome[-3]=='t' and nome[-2]=='x' and nome[-1]=='t'):
        print (f'{nome}')
    else:
        print(f'Não existe ficheiro')

def gera_nome(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    ficheiro = f.readlines()
    f.close()

    dic_numeros = {}
    for linha in ficheiro:
        palavra, numero = linha.split()
        dic_numeros[palavra] = eval(numero)

    with open('teste.json', 'w') as json_file:
        json.dump(dic_numeros, json_file, indent = 4)

    
#Chamar funções    
pede_nome("teste.txt")
gera_nome("teste.txt")




