import csv 
import json 
def csv_to_json (direccionCsv, direccionJson):
    arregloJson = []

    #leemos el csv
    with open (direccionCsv, encoding='utf-8-sig') as archivoCsv:
        lectorCsv = csv.DictReader(archivoCsv)

        # convetimos cada fila en un diccionario 
        for fila in lectorCsv:
            arregloJson.append(fila)
    
    #Convertimos el arreglo a un json 
    with open(direccionJson, 'w', encoding = 'utf-8-sig') as archivoJson:
        cadenaJson = json.dumps(arregloJson, ensure_ascii = False)
        archivoJson.write(cadenaJson)
