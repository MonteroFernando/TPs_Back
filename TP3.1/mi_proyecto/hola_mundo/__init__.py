from flask import Flask, jsonify, request
from config import Config
from datetime import datetime
from hola_mundo.static.applications import a_dict, bin_a_dec
import json

def init_app():

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    #Ejercicio1
    @app.route('/')
    def hola_mundo():
        return ("Bienvenidx!",200)
    #Ejercicio2
    @app.route('/info')
    def info():
        return (f'Bienvenidx a {Config.APP_NAME}',200)
    #Ejercicio3
    @app.route('/about')
    def about():
        response=jsonify(Config.description)
        response.headers['Content-Type']='application/json; charset=utf-8'
        return response,200
    #Ejercicio4
    @app.route('/suma/<int:nro1>/<int:nro2>')
    def suma(nro1,nro2):
        resultado=str(nro1 + nro2)
        return (resultado,200)
    #Ejercicio5
    @app.route('/age/<string:dob>')
    def age(dob):
        #comprueba si el formato ingresado es el correcto
        try:
            fech_nac=datetime.strptime(dob,'%Y-%m-%d').date()
        except ValueError:
            return (jsonify({'error':'el formato de fecha es incorrecto ISO 8601 (YYYY-MM-DD)'}),400)
        
        fech_act=datetime.now().date()
        #comprueba que la fecha ingresada no sea mayor a la fecha actual
        if fech_act<fech_nac:
            return (jsonify({'error':'La fecha ingresada no puede ser mayor a la fecha actual'}),400)
        
        edad=fech_act.year - fech_nac.year
        #comprueba si ya cumplio años
        if fech_act.month < fech_nac.month:
            edad+=1
        elif fech_act.month == fech_nac.month:
            if fech_act.day <= fech_nac.day:
                edad+=1
        
        return (str(edad),200)
    #Ejercicio6
    @app.route('/<string:operation>/<int:nro1>/<int:nro2>')
    def op(operation,nro1,nro2):
        if operation=='sum':
            resultado=nro1+nro2
        elif operation=='sub':
            resultado=nro1-nro2
        elif operation=='mult':
            resultado=nro1*nro2
        elif operation=='div':
            if nro2==0:
                return ('La división no esta definida para estos valores (No se puede dividir por 0)',400)
            else:
                resultado=nro1/nro2
        else:
            return (jsonify({'error':'No existe ruta definida para este endpoint'}),400)
        return (str(resultado),200)
    #Ejercicio6 (con fucniones lambda)
    """Otra manera de realizar el punto 6 es con funciones anonimas,
        queria dejar las dos opciones del ejercicio 6 la llamare "6v2" para diferenciarla de la primera version"""
    @app.route('/6v2/<string:operation>/<int:nro1>/<int:nro2>')
    def op2(operation,nro1,nro2):
        operations={
                    'sum':lambda x,y:x+y,
                    'sub':lambda x,y:x-y,
                    'mult':lambda x,y:x*y,
                    'div':lambda x,y: x/y if y!=0 else 'La división no esta definida para estos valores (No se puede dividir por 0)'
                    }
        if operation in operations:
            resultado=operations[operation](nro1,nro2)
        else:
            return (jsonify({'error':'No existe ruta definida para este endpoint'}),400)
        return (str(resultado),200)
    #Ejercicio7
    @app.route('/operate')
    def operate():
        operation=request.args.get('operation')
        nro1=int(request.args.get('nro1'))
        nro2=int(request.args.get('nro2'))
        operations={
                    'sum':lambda x,y:x+y,
                    'sub':lambda x,y:x-y,
                    'mult':lambda x,y:x*y,
                    'div':lambda x,y: x/y if y!=0 else 'La división no esta definida para estos valores (No se puede dividir por 0)'
                    }
        if operation in operations:
            resultado=operations[operation](nro1,nro2)
        else:
            return (jsonify({'error':'No existe ruta definida para este endpoint'}),400)
        return (str(resultado),200)
    #Ejercicio8
    @app.route('/title/<string:word>')
    def titulo(word):
        letras=list(word)
        for i in range(len(letras)):
            if i==0:
                letras[i]=letras[i].upper()
            else:
                letras[i]=letras[i].lower()
        word=''.join(letras)
        return (jsonify({'formatted_word':word}),200)
    #Ejercicio8 con el metodo .title() de python
    @app.route('/title2/<string:word>')
    def titulo2(word):
        titulo=word.title()
        return (jsonify({'formatted_word':titulo}),200)
    #Ejercicio9
    @app.route('/formatted/<string:dni>')
    def formatted(dni):
        cont=0
        nro=[]
        for d in dni:
            if d.isdigit():
                cont+=1
                nro.append(d)
        dni_formatted=int(''.join(nro))
        if len(str(dni_formatted))<8:
            return (jsonify({'error':'El dni ingresado contiene menos de 8 digitos'}),400)
        elif len(str(dni_formatted))>8:
            return (jsonify({'error':'El dni ingresado contiene mas de 8 digitos'}),400)
        else:
            return (jsonify({'formatted_dni':dni_formatted}),200)
    #Ejercicio10
    @app.route('/format')
    def format():
        firstname=request.args.get('firstname')
        lastname=request.args.get('lastname')
        date=request.args.get('dob')
        dni=request.args.get('dni')
        nombre_dict=titulo(firstname)[0].json
        nombre=nombre_dict['formatted_word']
        apellido_dict=titulo2(lastname)[0].json
        apellido=apellido_dict['formatted_word']
        try:
            date_dict=age(date)[0].json
            edad=date_dict['error']
        except:
            edad=age(date)[0]
        
        dni_dict=formatted(dni)[0].json
        if 'error' in dni_dict:
           documento= dni_dict['error']
        else:
           documento= dni_dict['formatted_dni']

        respuesta={'firstname':nombre,
                   'lastname':apellido,
                   'age':edad,
                   'dni':documento}
        return (jsonify(respuesta),200)
    #Ejercicio11
    @app.route('/encode/<string:keyword>')
    def encode(keyword):
        codigo_morse=a_dict('morse_code.json')
        list_encode=[]
        list_keyword=list(keyword)
        acentos=('á','é','í','ó','ú','ü')
        if list_keyword[0]==' ':
            return (jsonify({'error':'La palabra clave no debe iniciar con espacios'}),400)
        elif list_keyword[len(list_keyword)-1]==' ':
            return (jsonify({'error':'La palabra clave no debe finalizar con espacios'}),400)
        for i,leter in enumerate(list_keyword):
            if leter.lower() in acentos:
                return (jsonify({'error':'La palabra clave no debe contener palabras con tilde o diéresis'}),400)
            else:
                if leter == '+':
                    leter_up=' '
                else:
                    leter_up=leter.upper()
                list_encode.append(codigo_morse[leter_up])
                if i<len(list_keyword)-1:
                    list_encode.append('+')
        keyword_encode=''.join(list_encode)
        return(jsonify({'morse':keyword_encode}),200)
    #Ejercicio12
    @app.route('/decode/<string:morse_code>')
    def decode(morse_code):
        #Tomo el archivo .json como diccionario
        morse=a_dict('morse_code.json')
        #Creo una lista con los códigos separados
        codigo=morse_code.split("+")
        #de forma pythonica, invirtiendo el diccionario para tomar los valores como key
        morse_invert={val: key for key,val in morse.items()}
        #voy armando un una lista la palabra decodificada
        dec_list=[]
        for i,car in enumerate(codigo):
            if i==0:
                dec_list.append(morse_invert[car])
            elif i==len(codigo)-1:
                dec_list.append(morse_invert[car].lower())
                dec_list.append(".")

            else:
                dec_list.append(morse_invert[car].lower())

        decodificado="".join(dec_list)
        return (decodificado,200)
    #Ejercicio13
    @app.route('/convert/binary/<string:num>')
    def convert_binary(num):
        num_dec=bin_a_dec(num)
        return str(num_dec),200
    return app
    
    
