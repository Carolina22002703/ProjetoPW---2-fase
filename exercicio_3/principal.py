import os

def pede_pasta(nomePasta):
    #Pedir o caminho (relativo ou absoluto) de uma pasta para analisar. Se a pasta não existir, deverá pedir novamente. 
    #Esta função deverá retornar o caminho da pasta a analisar (se estiver na pasta exercicios_3 basta o nome da pasta, mas pode ser por exemplo C:\Users\lsf).

    if(os.path.exists(nomePasta)):
        print(nomePasta)
    else:
        print('Por favor tente novamente:')
        while True:
            nome = input("Introduza o caminho(relativo ou absoluto) de uma pasta? ")
            if(os.path.exists(nome)):
                print(nome)
                break
    

def calcula_tamanho_pasta(nomePasta):
    #Calcular o tamanho total em MBytes dos ficheiros nela contidos, tanto na pasta como nas sub-pastas

    #Pasta principal
    print(f'Tamanho da pasta : {(os.path.getsize(nomePasta))/2**20}')

    #Ficheiros nela contidos
    soma = 0
    print('Em pormenor:')
    for i in os.listdir(nomePasta):
        if(os.path.isfile(os.path.join(nomePasta,i))):
            soma += os.path.getsize(os.path.join(nomePasta, i))/2**20
            print(f'O ficheiro {i} da pasta {nomePasta} tem o seguinte tamanho: {(os.path.getsize(os.path.join(nomePasta, i)))/2**20}')
        elif(os.path.isdir(os.path.join(nomePasta,i))):
            soma += os.path.getsize(os.path.join(nomePasta, i))/2**20
            print(f'A pasta {i} da pasta {nomePasta} tem o seguinte tamanho: {(os.path.getsize(os.path.join(nomePasta, i)))/2**20}')
    print(f'Soma total de tamanhos dos ficheiros e pastas: {soma}')

#Chamar funções
if __name__ == '__main__':  
    pede_pasta("C:\\Users\carol\OneDrive\Ambiente de Trabalho\TRABALHOS\DERIVADOS")
    calcula_tamanho_pasta("C:\\Users\carol\OneDrive\Ambiente de Trabalho\TRABALHOS\DERIVADOS")