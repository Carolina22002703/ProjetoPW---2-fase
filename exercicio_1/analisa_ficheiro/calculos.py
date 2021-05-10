from collections import Counter

def calcula_linhas(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    ficheiro = f.readlines()
    f.close()

    #Contar quantas linhas
    count = 0
    for linha in ficheiro:
        count+=1
    print (f'Número de linhas: {count}')

def calcula_caracteres(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    ficheiro = f.read()
    f.close()

    #Contar quantos caracteres
    count1 = 0
    for i in ficheiro:
        count1+=1 
    print(f'Número de caracteres: {count1}')

def calcula_palavra_comprida(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    ficheiro = f.readlines()
    f.close()

    #Calcular a maior palavra
    dic_numeros = {}
    for linha in ficheiro:
        palavra, numero = linha.split()
        dic_numeros[palavra] = eval(numero)


    palavraMaior = ''
    for i in dic_numeros:
        primeira_posicao_palavra = i
        if(len(primeira_posicao_palavra)>len(palavraMaior)):
            palavraMaior=primeira_posicao_palavra
    print(f'Palavra maior: {palavraMaior}')

def calcula_ocorrencia_de_letras(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    ficheiro = f.read()
    f.close()

    #Calcular ocorrencias de letras
    counter = Counter(ficheiro)
    print(f'Dicionário de ocorrências: {counter}')
   
        
        
#Chamar funções
calcula_linhas("teste.txt")
calcula_caracteres("teste.txt")
calcula_palavra_comprida("teste.txt")
calcula_ocorrencia_de_letras("teste.txt")

