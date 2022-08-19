from bs4 import BeautifulSoup
import requests,random
links = []
url = 'https://books.toscrape.com/catalogue/page-1.html'
pagina = requests.get(url)


#raspagem dos links das imagens
soup = BeautifulSoup(pagina.text, 'html.parser') 
for item in soup.find_all('img'):
    links.append('https://books.toscrape.com/' + item['src']) 
links = list(set(links))

#download das imagens
for item in links:
        try:
            img_data = requests.get(item).content
            with open('{}.jpg'.format(random.randint(1,100000)), 'wb') as handler:
                handler.write(img_data)
        except:
            pass
