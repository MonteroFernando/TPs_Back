import json
import os

def ruta_static(file):
    '''Devuleve la ruta concatenando el archivo localizado en static'''
    #Se usa os.path.join para dar el formato del directorio del so donde se ejecuta
    ruta=os.path.join(os.getcwd(),'TP3.1','mi_proyecto','hola_mundo','static',file)
    return ruta

def a_dict(file):
    '''Funcion que retorna el diccionario de un archivo json ubicado en el directorio statics'''
    with open(ruta_static(file),'r') as json_file:
        dic=json.loads(json_file.read())
    return dic['letters']

def bin_a_dec(num):
    '''Funcion que convierte el string pasado como parametro de un numero bunario a decimal'''
    nro_dec=0
    for i,n in enumerate(num):
        exponente=(len(num)-(i+1))
        nro_dec+=int(n)*(2**exponente)
    return nro_dec
