from urllib.request import urlopen, urljoin
import re
def download_pagina(url): #função que irá baixar a página
 return urlopen(url).read().decode('utf-8')

def extrair_fonte(page): #função que irá extrair a fonte das imagens
 img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',
re.IGNORECASE)
 return img_regex.findall(page)

if __name__ == '__main__':
  for k in range(1,51):
     target_url = 'https://books.toscrape.com/catalogue/page-%d.html' %k
     page = download_pagina(target_url)
     image_locations = extrair_fonte(page)   
     k = open("links_imagens%d.txt" %k,"w")
     for src in image_locations: 
      k.write(urljoin(target_url, src) + "\n")
k.close()

