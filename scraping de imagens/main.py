from bs4 import BeautifulSoup
import requests,random
import re

url = 1
def find_png_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    png_links = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        if re.search(r'\.jpg$', href, re.IGNORECASE):
            png_links.append(href)

    return png_links


png_links = find_png_links(url)


#download das imagens
for item in png_links:
    try:
            response = requests.get(item)
            if response.status_code == 200:
                with open('{}.jpg'.format(random.randint(1,100000)), 'wb') as f:
                    f.write(response.content)
                    print(f"Imagem salva do link -> {item}")
            else:
                    print(f"Não foi possivel extrair a imagem de {item}")
    except:
        pass
