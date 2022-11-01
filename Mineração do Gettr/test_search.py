"""Tests for the 'search' capability."""

from gogettr import PublicClient
import pandas as pd
import datetime


client = PublicClient() #Criação do cliente

# busca = input("Digite palavra:")

def test_basic_search(query,max):
    """Realiza uma busca simples nos posts:
       Parametros: 
       query -> palavra que será pesquisada
       max -> Número maximo de posts que serão extraidos"""
    posts = list(client.search(query, max))
    return posts

def get_info(arg, column):    
    if 'uinf' in arg and column in arg['uinf']:
        return arg['uinf'][column]
    
    return None

def get_txt(arg):    
    if 'txt' in arg:
        return arg['txt']
    
    return None


def get_datetime(arg):    
    if 'udate' in arg:
        #my_datetime = datetime.datetime.fromtimestamp(arg['udate'] / 1000)         
        return arg['udate'] 
    
    return None


nome = input("-> Inserir palavra-chave:\n")

max = 800

var = test_basic_search(nome,max)

lista = []

print("quantidade de posts extraidos:",len(var))
try: 
    for k in range(max):        
    
        lista.append(
            {
                'username': get_info(var[k], 'username'),
                'nickname': get_info(var[k], 'nickname'),
                'ousername': get_info(var[k], 'ousername'),
                'website': get_info(var[k], 'website'),
                'location': get_info(var[k], 'location'),
                'datetime': get_datetime(var[k]),
                'txt': get_txt(var[k])
            }
            )
except:
    
    pass


df = pd.DataFrame(lista)
df.to_csv("%s.csv" %nome,index=False)
print("Extraído!!!!")
#username,location,txt,'nickname','ousername','website'