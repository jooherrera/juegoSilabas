from configuracion import *
from funcionesSeparador import *
import random
import math

#Retorna un array con las silabas/palabras que esten dentro del archivo.
def lectura(archivo, lista):
    lineas= archivo.readlines()
    for linea in lineas:
        if len(linea.strip()) >= LONG_MIN:
            lista.append(linea.strip())

#Recibe las silabas que estan en pantalla, sus posiciones,sus colores y la lista de todas las silabas.
#Elimina las sílabas y sus posiciones cuando empiza a escaparse de la pantalla.
def actualizar(silabasEnPantalla,posiciones,listaDeSilabas,width,height,segundos,coloresSilabas):
    randomX = random.randint(70,width-70)
    randomY = 0
    i = 0
    if (segundos <  15):
        velocidad = .5
    else:
        velocidad = 1
    if silabasEnPantalla == []:
        posiciones.append([randomX,randomY])
        addSilaba = nuevaSilaba(listaDeSilabas)
        silabasEnPantalla.append(addSilaba)
        coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    else:
        posYY= posiciones[len(silabasEnPantalla)-1][1]
        if posYY > 22  :
            posiciones.append([randomX,randomY])
            addSilaba = nuevaSilaba(listaDeSilabas)
            silabasEnPantalla.append(addSilaba)
            coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        else:
            while (i < len(silabasEnPantalla)):
                posY = posiciones[i][1]
                posiciones[i] = [posiciones[i][0],posiciones[i][1] + velocidad]

                if posY > floor(85.5*height/100):
                    quitar(0, silabasEnPantalla, posiciones,coloresSilabas)
                else:
                    i = i +1

#Retorna una silaba al azar, del array de silabas.
def nuevaSilaba(silabas):
    numero = random.randrange(len(silabas))
    silaba = silabas[numero]
    return silaba.lower()

#Elimina la silaba de la pantalla junto con su posición y su color.
def quitar(candidata, silabasEnPantalla, posiciones,coloresSilabas):
    silabasEnPantalla.pop(candidata)
    posiciones.pop(candidata)
    coloresSilabas.pop(candidata)

#Retorna una palabra separada en silabas.
def dameSilabas(candidata):
    return separador(candidata)

#Retorna TRUE si la palabra separada en silabas esta en la pantalla y se encuentra en el lemario.
def esValida(candidata, silabasEnPantalla, lemario,posiciones,coloresSilabas):

    palabraEnSilabas = ""
    palabraEnSilabas = dameSilabas(candidata)
    nuevaPalabra = arrayPalabraSeparada(palabraEnSilabas)

    if (estaEnPantalla(nuevaPalabra,silabasEnPantalla)):
        if (comprobarLemario(candidata,lemario)):
            silabasAEliminar(nuevaPalabra,silabasEnPantalla,posiciones,coloresSilabas)
            return True
        else:
            return False
    else:
        return False

#Retorna un valor dependiendo de las letras de la palabra.
def Puntos(candidata):
    puntos = 0
    vocales = "aeiou"
    dificiles = "jkqwxyz"

    for letra in candidata:
        if letra in vocales:
            puntos = puntos + 1
        elif letra in dificiles:
            puntos = puntos + 5
        else:
            puntos = puntos + 2
    return (puntos)

#Recibe la palabra escrita por el usuario y devuelve un puntaje.
def procesar(candidata, silabasEnPantalla, posiciones, lemario, coloresSilabas,reproducirSonido):

    if candidata != "exit":

        if (esValida(candidata,silabasEnPantalla,lemario,posiciones, coloresSilabas)):
            print("EsValida")
            totalPuntos = Puntos(candidata)
            if totalPuntos > 7 :
                reproducirSonido.play("muchosPuntos")
            else:
                reproducirSonido.play("acierto")
            return totalPuntos
        else:
            print("No existe")
            reproducirSonido.play("error")
            return 0
    else:
        return
##############################################################################

#Retorna un array de silabas de la palabra separada sin "guiones".
def arrayPalabraSeparada(palabraEnSilabas):
    silaba = ""
    nuevaPalabra = []
    for letra in palabraEnSilabas:
        if letra != "-":
            silaba = silaba + letra
        else:
            nuevaPalabra.append(silaba)
            silaba = ""
    return nuevaPalabra

#Retorna TRUE si encuentra la palabra separada en silabas en la pantalla.
def estaEnPantalla(nuevaPalabra,silabasEnPantalla):
    i = 0
    palabraArmada = ""
    for elemento in nuevaPalabra:
        if elemento in silabasEnPantalla:
            i = i + 1
            palabraArmada = palabraArmada + elemento
        else:
            return False
    if i == len(nuevaPalabra):
        return True
    else:
        return False

#Retorna TRUE si encuentra la palabra en el lemario.
def comprobarLemario(candidata,lemario):

    if candidata in lemario:
        return True
    else:
        return False

#Retorna un array con las posiciones para eliminar.
def silabasAEliminar(nuevaPalabra, silabasEnPantalla, posiciones,coloresSilabas):
    for elemento in nuevaPalabra:
        if elemento in silabasEnPantalla:
            quitar(silabasEnPantalla.index(elemento),silabasEnPantalla,posiciones,coloresSilabas)