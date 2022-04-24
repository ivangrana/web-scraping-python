import requests
import re

#Extração de links de imagens de uma página

url = input("Inserir URL -> ")

var = requests.get(url).text

print("Links de imagens:")
for image in re.findall("<img (.*)>",var):
    for images in image.split():
        if re.findall("src=(.*)",images):
            image = images[:-1].replace("src=\"","")
        if(image.startswith("http")):
            print(image)
