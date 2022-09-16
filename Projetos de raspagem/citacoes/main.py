from aux_1 import raspar_texto
#Scraping de citações de autores e pensadores

if __name__ == '__main__':
    nome_autor = input("Insira o nome do(a) autor(a) ou pensador(a)")
    for num_pagina in (1,3):
        print(raspar_texto('https://www.pensador.com/autor/charles_chaplin/{}'.format(num_pagina)))
        