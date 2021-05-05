def calcula_linhas(nome):
    #Abertura do ficheiro e colocação numa lista
    f = open(nome)
    nome = f.read()
    f.close()

    #Contar quantas linhas
    count = 0
    for i in nome.split('\n'):
        count+=1
    print (f'{count}')

calcula_linhas("teste.txt")