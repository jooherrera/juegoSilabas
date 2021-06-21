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

def lectura2(archivo, lista):
    lineas= archivo.readlines()
    for linea in lineas:
        lista.append(int(linea.strip()))

    return lista

#Actualiza la pantalla.
def actualizar(silabasEnPantalla,posiciones,listaDeSilabas,width,height,segundos,coloresSilabas):
    randomX = random.randint(70,width-70) #Numero aleatorio para la posicion X.
    randomY = 0  #Numero para la posicion Y.
    i = 0


    if (segundos <  15):
        velocidad = .5
    else:
        velocidad = 1




    if silabasEnPantalla == []:
        posiciones.append([randomX,randomY]) #Agrega las posiciones (x,y) en un array.
        addSilaba = nuevaSilaba(listaDeSilabas) #Busca una silaba al azar.
        silabasEnPantalla.append(addSilaba) #Agrega la silaba del azar a un array quitandole los espacios.
        coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    else:
        posYY= posiciones[len(silabasEnPantalla)-1][1]
        print(posYY)

        if posYY > 22  :
            posiciones.append([randomX,randomY]) #Agrega las posiciones (x,y) en un array.
            addSilaba = nuevaSilaba(listaDeSilabas) #Busca una silaba al azar.
            silabasEnPantalla.append(addSilaba) #Agrega la silaba del azar a un array quitandole los espacios.
            coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        else:


            while (i < len(silabasEnPantalla)):
                posY = posiciones[i][1] #Guarda la posicion en Y de los elementos en pantalla.
                posiciones[i] = [posiciones[i][0],posiciones[i][1] + velocidad] #Actualiza la posicion en  Y de los elementos en pantalla.

                if posY > floor(85.5*height/100):  #Comprueba que la posicion Y del elemento es mayor a 500.
                    silabasEnPantalla.pop(0) #Elimila del array la silaba que se esta mostrando.
                    posiciones.pop(0) #Elimina del array la posicion de la silaba.
                    coloresSilabas.pop(0)
                    #elif posiciones[len(posiciones)-1][1] > 100:
        #        if posiciones[len(silabasEnPantalla)-1][1] > 120:
                else:
                    i = i +1 #aumenta contador para el ciclo while





#Retorna una silaba al azar, del array de silabas.
def nuevaSilaba(silabas):
    #return silabas[random.randint(0,len(silabas)-1)] #Random de 0 a logitud del array.
    return silabas[random.randrange(len(silabas))] #Random de 0 a logitud del array.

#Elimina la silaba de la pantalla
def quitar(candidata, silabasEnPantalla, posiciones,coloresSilabas):
    print(candidata)
    silabasEnPantalla.pop(candidata) #Elimila del array la silaba que se esta mostrando.

    posiciones.pop(candidata) #Elimina del array la posicion de la silaba.
    coloresSilabas.pop(candidata)
    #return silabasEnPantalla,posiciones #Retorna los arrays actualizados.

#Retorna una palabra separada en silabas.
def dameSilabas(candidata):
    return separador(candidata)

#Retorna TRUE si la palabra separada en silabas esta en la pantalla y se encuentra en el lemario.
def esValida(candidata, silabasEnPantalla, lemario,posiciones,coloresSilabas):

    palabraEnSilabas = ""
    palabraEnSilabas = dameSilabas(candidata) #Se guarda la palabra separada en silabas.
    nuevaPalabra = arrayPalabraSeparada(palabraEnSilabas) #Se guarda las silabas separadas en un array.

    if (estaEnPantalla(nuevaPalabra,silabasEnPantalla)): #Busca si esta en pantalla las silabas.
        if (comprobarLemario(candidata,lemario)): #Comprueba que la palabra esté en el lemario.
            silabasAEliminar(nuevaPalabra,silabasEnPantalla,posiciones,coloresSilabas) #Busca las posiciones de las silabas y las guarda en un array.
            return True
        else:
            return False
    else:
        return False

#Retorna un valor dependiendo de las letras de la palabra.
def Puntos(candidata):
    puntos = 0 #Se inicializa la variable a retornar.
    vocales = "aeiou" #Se guardan las vocales.
    dificiles = "jkqwxyz" #Se guardan las consonantes dificiles.


    for letra in candidata: #Busca letra por letra en la palabra.
        if letra in vocales: #Si la letra es una vocal.
            puntos = puntos + 1 #Suma un punto.
        elif letra in dificiles: #Si la letra es una consonante difícil.
            puntos = puntos + 5 #Suma dos puntos.
        else:
            puntos = puntos + 2 #Suma tres puntos.
    return (puntos) #Retorna el puntaje obtenido.

#Recibe la palabra escrita por el usuario y devuelve un puntaje.
def procesar(candidata, silabasEnPantalla, posiciones, lemario, coloresSilabas):

    if (esValida(candidata,silabasEnPantalla,lemario,posiciones, coloresSilabas)): #Si en la pantalla estan todas las silabas de la palabra y esta en el lemario.
        print("EsValida")
        return Puntos(candidata)#Retorna un puntaje.
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
def silabasAEliminar(nuevaPalabra, silabasEnPantalla, posiciones,coloresSilabas):
    #listaParaEliminar = [] #Inicializa una lista para guardar las posiciones (En el array) que tienen las silabas que estan en la pantalla
    for elemento in nuevaPalabra: #Comprueba los elementos del array
        print("Elemento para eliminar",elemento)
        if elemento in silabasEnPantalla: #Si encuentra el elemento en el array que esta mostrando la pantalla.
            quitar(silabasEnPantalla.index(elemento),silabasEnPantalla,posiciones,coloresSilabas) #Agrega la posicion que tiene en la lista para despues eliminarlo.
    #return listaParaEliminar #Retorna el array.


