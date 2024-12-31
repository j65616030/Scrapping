import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# URL del sitio web a scrapear
url = "https://www.ejemplo.com"

# Realizar una petición GET al sitio web
response = requests.get(url)

# Si la petición es exitosa, el estado de la respuesta será 200
if response.status_code == 200:
    # Obtener el contenido HTML de la respuesta
    html = response.text

    # Parsear el HTML utilizando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extraer la información que deseas scrapear
    # Por ejemplo, extraer todos los títulos de las noticias
    titulos = soup.find_all('h2')

    # Crear un archivo .txt para guardar la información
    with open('informacion.txt', 'w') as archivo_txt:
        for titulo in titulos:
            archivo_txt.write(titulo.text + '\n')

    # Crear un archivo .xml para guardar la información
    raiz = ET.Element('noticias')
    for titulo in titulos:
        noticia = ET.SubElement(raiz, 'noticia')
        ET.SubElement(noticia, 'titulo').text = titulo.text

    arbol = ET.ElementTree(raiz)
    arbol.write('informacion.xml')

    print("Información guardada en archivos .txt y .xml")
else:
    print("Error al realizar la petición GET")
