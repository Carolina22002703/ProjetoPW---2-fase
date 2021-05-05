def pede_nome(nome):
    if (nome[:-3] == "txt"):
        print (f'{nome}')
    else:
        print(f'Não existe ficheiro')
    
pede_nome("teste.txt")


