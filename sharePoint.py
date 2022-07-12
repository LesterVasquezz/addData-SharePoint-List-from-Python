from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

from excelToJson import csv_to_json
import json

#convertimos csv a json
csv_to_json('dataset.csv', 'salida.json')

#obtenemos los datos del json 
archivo = open('salida.json', encoding = "utf-8-sig")
datos = json.load(archivo)

#Conectamos al sharepoint via REST API

authcookie = Office365('https://domain.sharepoint.com', username='email@email.com', password='pass').GetCookies()

site = Site('https://domain.sharepoint.com/sites/your-site/', version=Version.v365, authcookie=authcookie)


#site.AddList('Oaxaca', description='Municipios en Oaxaca', template_id='Custom List')


archivo = open('salida.json', encoding = "utf-8-sig")
datos = json.load(archivo)

site.List('Oaxaca').update_list_items(data=datos, kind='New')


