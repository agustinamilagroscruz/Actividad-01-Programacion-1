"""
Módulo: utilidades.py
Descripción: Contiene funciones auxiliares reutilizables para dar formato tabular
a la información mostrada en pantalla.
Materia: Programación 1 - FAIN UADE
"""


def calcular_ancho_texto(matriz, columna, encabezado):
    ancho = len(encabezado)

    for i in range(len(matriz)):
        if len(str(matriz[i][columna])) > ancho:
            ancho = len(str(matriz[i][columna]))

    return ancho + 3


def completar_espacios(texto, ancho):
    cantidad_espacios = ancho - len(str(texto))
    texto_con_espacios = str(texto) + " " * cantidad_espacios

    return texto_con_espacios
