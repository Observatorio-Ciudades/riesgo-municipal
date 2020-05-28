################################################################################
# Module: Data downloader
# Saves the data from Secretaria de Salud in the folder ../data/raw/{date}.{format}
# developed by: Edgar Egurrola
# 			  edgar.egurrola@tec.mx
# updated: 28/05/2020
################################################################################

import os
import sys

import requests
import zipfile
from datetime import date
from datetime import timedelta
#import src

def covid_mun ():
    """Download csv file with daily updates from the Secretaria de Salud about COVID-19 by municipality
    
    """

    #Saved data location
    ubicacion = 'D:\\Users\\edgar\\Source\\Repos\\Observatorio-Ciudades\\riesgo-municipal\\data\\raw\\municipalities\\'+str(date.today()-timedelta(days=1))
    os.mkdir(ubicacion) 

    #data download url
    url = 'http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'

    r = requests.get(url)

    #Name and location to save data
    archivo = ubicacion + '\\' + 'datos_abiertos_covid19.zip'

    #Escribe el archivo zip
    with open (archivo, 'wb') as code:
        code.write(r.content)

    #Escribe el archivo zip
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        zip_ref.extractall(ubicacion)
