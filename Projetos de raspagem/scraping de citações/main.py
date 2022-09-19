from aux_1 import raspar_texto
#Scraping de citações de autores e pensadores
#Autor: Ivan Grana

if __name__ == '__main__':
    nome_autor = input("Insira o nome do(a) autor(a) ou pensador(a):\n->")
    nome_autor = nome_autor.replace(" ","_")
    print("Citações de %s extraidas" %nome_autor.replace("_"," "))
    print("-"*60)
    for num_pagina in (1,3):
        print(raspar_texto('https://www.pensador.com/autor/{}/{}'.format(nome_autor,num_pagina)))
    print("-"*60)
    print("fim da extração !")
