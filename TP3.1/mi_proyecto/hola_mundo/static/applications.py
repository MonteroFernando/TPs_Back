import json
import os

def ruta_static(file):
    '''Devuleve la ruta concatenando el archivo localizado en static'''
    #Se usa os.path.join para dar el formato del directorio del so donde se ejecuta
    ruta=os.path.join(os.getcwd(),'hola_mundo','static',file)
    return ruta

def a_dict(file):
    '''Funcion que retorna el diccionario de un archivo json ubicado en el directorio statics'''
    with open(ruta_static(file),'r') as json_file:
        dic=json.loads(json_file.read())
    return dic['letters']



