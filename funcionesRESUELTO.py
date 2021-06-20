from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math



#Retorna un array con las silabas/palabras que esten dentro del archivo.
def lectura(archivo, lista):
    lineas= archivo.readlines()
    for linea in lineas:
        lista.append(linea.strip())

    return lista
def lectura2(archivo, lista):
    lineas= archivo.readlines()
    for linea in lineas:
        lista.append(int(linea.strip()))

    return lista

#Actualiza la pantalla.
def actualizar(silabasEnPantalla,posiciones,listaDeSilabas,width,height):
    randomX = random.randint(70,width-70) #Numero aleatorio para la posicion X.
    randomY = -50  #Numero para la posicion Y.

    posiciones.append([randomX,randomY]) #Agrega las posiciones (x,y) en un array.
    addSilaba = nuevaSilaba(listaDeSilabas) #Busca una silaba al azar.
    silabasEnPantalla.append(addSilaba) #Agrega la silaba del azar a un array.

    listaParaEliminar = [] #Array nuevo donde se guardan las posiciones de los elementos a eliminar.
    for i in range(0,len(posiciones)):
        posY = posiciones[i][1] #Guarda la posicion en Y de los elementos en pantalla.
        posiciones[i] = [posiciones[i][0],posiciones[i][1] + 25] #Actualiza la posicion en  Y de los elementos en pantalla.

        if posY > floor(80*height/100):  #Comprueba que la posicion Y del elemento es mayor a 500. 480
            listaParaEliminar.append(i) #Se agrega al array la ubicacion original del elemento a eliminar.



    for posicionParaEliminar in listaParaEliminar: #Buscar todos los elementos a eliminar.
        print(posicionParaEliminar)

        quitar(posicionParaEliminar,silabasEnPantalla,posiciones) #Quita elementos y actualiza los arrays.

    #return silabasEnPantalla,posiciones #Retorna las silabas en pantalla y sus posiciones.

#Retorna una silaba al azar, del array de silabas.
def nuevaSilaba(silabas):
    #return silabas[random.randint(0,len(silabas)-1)] #Random de 0 a logitud del array.
    return silabas[random.randrange(len(silabas))] #Random de 0 a logitud del array.

#Elimina la silaba de la pantalla
def quitar(candidata, silabasEnPantalla, posiciones):
    print(candidata)
    silabasEnPantalla.pop(candidata) #Elimila del array la silaba que se esta mostrando.

    posiciones.pop(candidata) #Elimina del array la posicion de la silaba.
    #return silabasEnPantalla,posiciones #Retorna los arrays actualizados.

#Retorna una palabra separada en silabas.
def dameSilabas(candidata):
    return separador(candidata)

#Retorna TRUE si la palabra separada en silabas esta en la pantalla y se encuentra en el lemario.
def esValida(candidata, silabasEnPantalla, lemario,posiciones):

    palabraEnSilabas = ""
    palabraEnSilabas = dameSilabas(candidata) #Se guarda la palabra separada en silabas.
    nuevaPalabra = arrayPalabraSeparada(palabraEnSilabas) #Se guarda las silabas separadas en un array.
    palabraArmada = ""
    listaParaEliminar = [] #Array para guardar las posiciones de las silabas encontradas.

    if (estaEnPantalla(nuevaPalabra,silabasEnPantalla)): #Busca si esta en pantalla las silabas.
        if (comprobarLemario(candidata,lemario)): #Comprueba que la palabra esté en el lemario.
            #listaParaEliminar = armarArrayParaEliminar(nuevaPalabra,silabasEnPantalla) #Busca las posiciones de las silabas y las guarda en un array.
            armarArrayParaEliminar(nuevaPalabra,silabasEnPantalla,listaParaEliminar) #Busca las posiciones de las silabas y las guarda en un array.
            for element in listaParaEliminar: #Busca todos los elementos a eliminar.
                quitar(element,silabasEnPantalla,posiciones) #Quita elementos y actualiza los arrays.
            return True
        else:
            return False
    else:
        return False

#Retorna un valor dependiendo de las letras de la palabra.
def Puntos(candidata):
    vocales = "aeiou" #Se guardan las vocales.
    comunes = "bcdfghlmnñprstv" #Se guardan las consonantes comunes.
    dificiles = "jkqwxyz" #Se guardan las consonantes dificiles.
    puntos = 0 #Se inicializa la variable a retornar.

    for letra in candidata: #Busca letra por letra en la palabra.
        if letra in vocales: #Si la letra es una vocal.
            puntos = puntos + 1 #Suma un punto.
        elif letra in dificiles: #Si la letra es una consonante común.
            puntos = puntos + 5 #Suma dos puntos.
        else: #Si la letra es una consonante dificil.
            puntos = puntos +2 #Suma tres puntos.
    return puntos #Retorna el puntaje obtenido.

#Recibe la palabra escrita por el usuario y devuelve un puntaje.
def procesar(candidata, silabasEnPantalla, posiciones, lemario):

    if (esValida(candidata,silabasEnPantalla,lemario,posiciones)): #Si en la pantalla estan todas las silabas de la palabra y esta en el lemario.
        print("EsValida")
        return int(Puntos(candidata)) #Retorna un puntaje.
    else:
        print("No existe")
        return 0 #Si no lo encuentra retorna de puntaje 0

##############################################################################

#Retorna un array de silabas de la palabra separada por "guiones".
def arrayPalabraSeparada(palabraEnSilabas):
    silaba = "" #Inicializa la variable para formar las silabas.
    nuevaPalabra = [] #Inicializa la variable para retornar un array.
    for letra in palabraEnSilabas: #Se busca letra por letra.
        if letra != "-": #Busca que la letra no sea un guion.
            silaba = silaba + letra #Agrega la letra para formar una silaba
        else:
            #Si encuentra un guion.
            nuevaPalabra.append(silaba) #Agrega al array la silaba armada.
            silaba = "" #Reinicia la variable para seguir armando la silaba.
    return nuevaPalabra #Retorna la parabra separada en un array.

#Retorna TRUE si encuentra la palabra separada en silabas en la pantalla.
def estaEnPantalla(nuevaPalabra,silabasEnPantalla):
    i = 0 #Inicializa contador de elementos.
    palabraArmada = "" #Inicializa la variable para volver a armar la palabra.
    for elemento in nuevaPalabra: #Recorre la palabra que esta separada en un array.
        if elemento in silabasEnPantalla: #Busca si el elemento esta en la pantalla.
            i = i + 1 #Aumenta cada vez que encuentra al elemento en pantalla.
            palabraArmada = palabraArmada + elemento #Arma la palabra sin separaciones.
        else:
            #Si no lo encuentra retorna FALSE.
            return False

    if i == len(nuevaPalabra): #Si el contador es igual a la longitud del array que tiene las silabas.
        return True #Retorna si encontro todas las silabas en pantalla.
    else:
        return False

#Retorna TRUE si encuentra la palabra en el lemario.
def comprobarLemario(candidata,lemario):

    if candidata in lemario: #Busca la palabra en el lemario.
        return True               #Se agrega \n por los saltos de linea.
    else:
        return False

#Retorna un array con las posiciones para eliminar.
def armarArrayParaEliminar(nuevaPalabra, silabasEnPantalla, listaParaEliminar):
    #listaParaEliminar = [] #Inicializa una lista para guardar las posiciones (En el array) que tienen las silabas que estan en la pantalla
    for elemento in nuevaPalabra: #Comprueba los elementos del array
       if elemento in silabasEnPantalla: #Si encuentra el elemento en el array que esta mostrando la pantalla.
            listaParaEliminar.append(silabasEnPantalla.index(elemento)) #Agrega la posicion que tiene en la lista para despues eliminarlo.
    #return listaParaEliminar #Retorna el array.