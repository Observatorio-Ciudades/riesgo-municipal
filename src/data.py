import requests
import zipfile

#Ubicacion para guardar el archivo
ubicacion = 'D:\\Users\\edgar\\Source\\Repos\\Observatorio-Ciudades\\riesgo-municipal\\data\\raw'

#url para descargar el archivo
url = 'http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'

r = requests.get(url)

#Nombre del archivo y ubicacion en el que se guarda el zip
archivo = ubicacion + '\\' + 'datos_abiertos_covid19.zip'

#Escribe el archivo zip
with open (archivo, 'wb') as code:
	code.write(r.content)

#Escribe el archivo zip
with zipfile.ZipFile(archivo, 'r') as zip_ref:
	zip_ref.extractall(ubicacion)
