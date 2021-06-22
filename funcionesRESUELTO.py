#from principal import *
from configuracion import *
from funcionesSeparador import *
import random
import math



#Retorna un array con las silabas/palabras que esten dentro del archivo.
def lectura(archivo, lista):
    lineas= archivo.readlines()#Lee cada linea del archivo abierto.
    for linea in lineas: #Recorre li linea por linea.
        if len(linea.strip()) >= LONG_MIN: #Solo agrega las sílabas dependiendo de la longitud que se le paso en la configuración.
            lista.append(linea.strip())#Agrega a lista todas las lineas del archivo que cumplen la condicion de longitud. .strip() borra los espacios en blanco antes y despues. se le agrega por que imprimia en pantalla \n


#Actualiza la pantalla.
def actualizar(silabasEnPantalla,posiciones,listaDeSilabas,width,height,segundos,coloresSilabas):
    randomX = random.randint(70,width-70) #Numero aleatorio para la posicion X.
    randomY = 0  #Numero para la posicion Y.
    i = 0 #Inicializa contador para el ciclo while.


    if (segundos <  15): # Si los segundos es menor a 15
        velocidad = .5 # Si es True - la velocidad con la que bajan las silabas es .5
    else:
        velocidad = 1   # Si es False - la velocidad con la que bajan las silabas es 1




    if silabasEnPantalla == []:  #### Esto se ejecuta una vez.. por que silabas en pantalla empieza vacia.
        posiciones.append([randomX,randomY]) #Agrega las posiciones (x,y) en un array.
        addSilaba = nuevaSilaba(listaDeSilabas) #Busca una silaba al azar.
        silabasEnPantalla.append(addSilaba) #Agrega la silaba del azar a un array quitandole los espacios.
        coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])#Agrega un color al azar a un array.

    else: # sino esta vacia silabasEnPantalla
        posYY= posiciones[len(silabasEnPantalla)-1][1]# Compruebo la posición de la ultima silaba que está en pantalla.
        if posYY > 22  :#Si la posición es mayor a 22 agrega otra silaba a la lista.
            posiciones.append([randomX,randomY]) #Agrega las posiciones (x,y) en un array.
            addSilaba = nuevaSilaba(listaDeSilabas) #Busca una silaba al azar.
            silabasEnPantalla.append(addSilaba) #Agrega la silaba del azar a un array quitandole los espacios.
            coloresSilabas.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])#Agrega un color al azar a un array.
        else:# Si la ultima silaba no supero los 22..


            while (i < len(silabasEnPantalla)):
                posY = posiciones[i][1] #Guarda la posicion en Y de los elementos en pantalla.
                posiciones[i] = [posiciones[i][0],posiciones[i][1] + velocidad] #Actualiza la posicion en  Y de los elementos en pantalla.

                if posY > floor(85.5*height/100):  #Comprueba SI la posicion Y del elemento supera un cierto numero de pixel.
                    quitar(0, silabasEnPantalla, posiciones,coloresSilabas) #Llama a la funcion Quitar para elimiar el elemento de las listas.
                                                                            #se le pasa 0 porque es el primer elemento que esta pasando la linea
                                                                            #de limite para que se empiezen a borrar.
                else:
                    i = i +1 #aumenta contador para el ciclo while





#Retorna una silaba al azar, del array de silabas.
def nuevaSilaba(silabas):
    numero = random.randrange(len(silabas)) # Guarda en numero un numero aleatorio de 0 a el total de silabas en la lista
    silaba = silabas[numero] #Guarda en silaba una al azar de la lista de silabas.
    return silaba.lower() #Retorna la silaba en minuscula.

#Elimina la silaba de la pantalla
def quitar(candidata, silabasEnPantalla, posiciones,coloresSilabas):
    silabasEnPantalla.pop(candidata) #Elimila del array la silaba que se esta mostrando.
    posiciones.pop(candidata) #Elimina del array la posicion de la silaba.
    coloresSilabas.pop(candidata)#Elimina del array el color de la silaba.


#Retorna una palabra separada en silabas.
def dameSilabas(candidata):
    return separador(candidata) # Llama a separador y le pasa la candidata.

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
def procesar(candidata, silabasEnPantalla, posiciones, lemario, coloresSilabas,reproducirSonido):

    if candidata != "exit": #Comprueba que la palabra que se escribio para comprobar no esa EXIT

        if (esValida(candidata,silabasEnPantalla,lemario,posiciones, coloresSilabas)): #Si en la pantalla estan todas las silabas de la palabra y esta en el lemario.
            print("EsValida")
            totalPuntos = Puntos(candidata) #Recibe el puntaje de la palabra armada.
            if totalPuntos > 7 : # Si el puntaje es mayor a 7...
                reproducirSonido.play("muchosPuntos") #Reproduce un sonido de acierto.
            else: # Sino
                reproducirSonido.play("acierto") #Reproduce otro sonido de acierto.
            return totalPuntos#Retorna un puntaje.
        else: #Si no es valida
            print("No existe")
            reproducirSonido.play("error") #Reproduce un sonido de error.
            return 0 #Si no lo encuentra retorna de puntaje 0.
    else: # Si la palabra que ingreso es EXIT vuelve a la pantalla anterior.
        return #Regresa a la pantalla anterior
##############################################################################

#Retorna un array de silabas de la palabra separada por "guiones".
def arrayPalabraSeparada(palabraEnSilabas):
    silaba = "" #Inicializa la variable para formar las silabas.
    nuevaPalabra = [] #Inicializa la variable para retornar un array.
    for letra in palabraEnSilabas: #Se busca letra por letra.
        if letra != "-": #Busca que la letra no sea un guion.
            silaba = silaba + letra #Agrega la letra para formar una silaba
        else: #Sino...
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
        return True       #Retorna True si lo encuentra.
    else:
        return False       #Retorna False si no lo encuentra

#Retorna un array con las posiciones para eliminar.
def silabasAEliminar(nuevaPalabra, silabasEnPantalla, posiciones,coloresSilabas):
    #listaParaEliminar = [] #Inicializa una lista para guardar las posiciones (En el array) que tienen las silabas que estan en la pantalla
    for elemento in nuevaPalabra: #Comprueba los elementos del array
        if elemento in silabasEnPantalla: #Si encuentra el elemento en el array que esta mostrando la pantalla.
            quitar(silabasEnPantalla.index(elemento),silabasEnPantalla,posiciones,coloresSilabas) #Agrega la posicion que tiene en la lista para despues eliminarlo.


