from bs4 import BeautifulSoup
import pandas as pd
import re

df = pd.read_csv('Alumnos.csv')
alumnos = []

for element in df['codigo']:
    alumno = []
    alumno.append(element)
    HTMLFileToBeOpened = open("Sócrates - Intranet Notas Alumno_files\ic0900o.html", "r")
    contents = HTMLFileToBeOpened.read()
    soup = BeautifulSoup(contents, 'html.parser')
    #Promedio acumulado
    info = soup.find_all('font')
    s = info[32].text
    result = re.search("acumulado (.*). Orden", s).group(1)
    alumno.append(result)
    #Nivel de inglés
    info = soup.find_all('font')
    s = info[35].text
    result = re.search("cumplido: (.*).", s).group(1)
    alumno.append(result[0:2])
    alumnos.append(alumno)

df = pd.DataFrame(alumnos, columns = ['codigo', 'promedio acumulado', 'nivel de ingles'])
df.to_csv('Resultado.csv', index=False)

