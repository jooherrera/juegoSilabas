from collections import namedtuple
from math import floor

FPS_inicial = 60
TIEMPO_MAX = 61

COLOR_LETRAS = (20,200,20)
COLOR_FONDO = (0,0,0)
COLOR_TEXTO = (200,200,200)
COLOR_TIEMPO_FINAL = (200,20,10)
Punto = namedtuple('Punto','x y')
RED = (255,0,0) #Color Rojo
BLUE= (0,0,255) #Color Azul
LONG_MIN = 2 # Longitud minima de la silaba para cargar en la lista.

Width = 1024 # Ancho por default
Height = 768 # Alto por default

GITHUBcollider = (floor(91.4*Width/100),floor(89.5*Height/100))# Variable para la detección del logo de Github
GITHUBcolliderW_H = (floor(6*Width/100),floor(7.8*Height/100))# Variable para la detección del logo de Github