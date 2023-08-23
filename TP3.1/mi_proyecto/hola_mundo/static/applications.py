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

class Pila():
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0
    
def ver_pila(cadena):
    pila = Pila()
    simbolos_apertura = "([{"
    simbolos_cierre = ")]}"
    
    for simbolo in cadena:
        if simbolo in simbolos_apertura:
            pila.push(simbolo)
        elif simbolo in simbolos_cierre:
            if pila.isEmpty():
                return False
            simbolo_apertura = pila.pop()
            if (simbolo == ')' and simbolo_apertura != '(') or \
               (simbolo == ']' and simbolo_apertura != '[') or \
               (simbolo == '}' and simbolo_apertura != '{'):
                return False
    
    return pila.isEmpty()
