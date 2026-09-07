"""
Módulo: consultas.py
Descripción: Contiene el listado general de productos y la consulta filtrada
por categoría.
Materia: Programación 1 - FAIN UADE
"""

from utilidades import calcular_ancho_texto, completar_espacios
from validaciones import seleccionar_categoria


def mostrar_todos_los_registros(matriz):
    """
    Imprime un listado completo de los productos en formato tabular con columnas alineadas.

    Parámetros:
        matriz (list): Matriz de productos.
    """
    print()
    print("=" * 80)
    print("                    LISTADO GENERAL DE INVENTARIO")
    print("=" * 80)

    if len(matriz) == 0:
        print(">> No hay productos para mostrar en el inventario.")
        print("=" * 80)
        return

    ancho_codigo = calcular_ancho_texto(matriz, 0, "CÓDIGO")
    ancho_nombre = calcular_ancho_texto(matriz, 1, "NOMBRE")
    ancho_categoria = calcular_ancho_texto(matriz, 2, "CATEGORÍA")
    ancho_precio = calcular_ancho_texto(matriz, 3, "PRECIO")
    ancho_stock = calcular_ancho_texto(matriz, 4, "STOCK")

    print(completar_espacios("CÓDIGO", ancho_codigo), end="")
    print(completar_espacios("NOMBRE", ancho_nombre), end="")
    print(completar_espacios("CATEGORÍA", ancho_categoria), end="")
    print(completar_espacios("PRECIO", ancho_precio), end="")
    print(completar_espacios("STOCK", ancho_stock))

    for i in range(len(matriz)):
        print(completar_espacios(matriz[i][0], ancho_codigo), end="")
        print(completar_espacios(matriz[i][1], ancho_nombre), end="")
        print(completar_espacios(matriz[i][2], ancho_categoria), end="")
        print(completar_espacios(matriz[i][3], ancho_precio), end="")
        print(completar_espacios(matriz[i][4], ancho_stock))

    print("=" * 80)
    print("Total de productos en lista:", len(matriz))


def consultar_por_categoria(matriz, categorias):
    """
    Permite seleccionar una categoría y muestra todos los productos pertenecientes a la misma.

    Parámetros:
        matriz (list): Matriz de productos.
        categorias (list): Lista de categorías válidas.
    """
    print()
    print("=" * 80)
    print("             CONSULTA DE PRODUCTOS POR CATEGORÍA")
    print("=" * 80)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        print("=" * 80)
        return

    categoria_seleccionada = seleccionar_categoria(categorias)
    print()
    print("PRODUCTOS EN LA CATEGORÍA:", categoria_seleccionada)

    ancho_codigo = calcular_ancho_texto(matriz, 0, "CÓDIGO")
    ancho_nombre = calcular_ancho_texto(matriz, 1, "NOMBRE")
    ancho_categoria = calcular_ancho_texto(matriz, 2, "CATEGORÍA")
    ancho_precio = calcular_ancho_texto(matriz, 3, "PRECIO")
    ancho_stock = calcular_ancho_texto(matriz, 4, "STOCK")

    print(completar_espacios("CÓDIGO", ancho_codigo), end="")
    print(completar_espacios("NOMBRE", ancho_nombre), end="")
    print(completar_espacios("CATEGORÍA", ancho_categoria), end="")
    print(completar_espacios("PRECIO", ancho_precio), end="")
    print(completar_espacios("STOCK", ancho_stock))

    encontrados = 0

    for i in range(len(matriz)):
        if matriz[i][2] == categoria_seleccionada:
            print(completar_espacios(matriz[i][0], ancho_codigo), end="")
            print(completar_espacios(matriz[i][1], ancho_nombre), end="")
            print(completar_espacios(matriz[i][2], ancho_categoria), end="")
            print(completar_espacios(matriz[i][3], ancho_precio), end="")
            print(completar_espacios(matriz[i][4], ancho_stock))
            encontrados += 1

    print("=" * 80)

    if encontrados == 0:
        print(">> No se encontraron productos registrados en la categoría", categoria_seleccionada)
    else:
        print("Total de productos encontrados en", categoria_seleccionada, ":", encontrados)
