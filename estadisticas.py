"""
Módulo: estadisticas.py
Descripción: Contiene las funciones para el cálculo y procesamiento estadístico
de los registros almacenados en la matriz de inventario.
Materia: Programación 1 - FAIN UADE
"""

import validaciones


def calcular_total_registros(matriz):
    """
    Calcula la cantidad total de productos almacenados en la matriz.
    
    Parámetros:
        matriz (list): Matriz de productos.
        
    Retorna:
        int: Cantidad total de registros.
    """
    return len(matriz)


def contar_registros_por_categoria(matriz, categoria):
    """
    Calcula la cantidad de productos pertenecientes a una categoría específica.
    
    Parámetros:
        matriz (list): Matriz de productos.
        categoria (str): Nombre de la categoría a contabilizar.
        
    Retorna:
        int: Cantidad de productos en dicha categoría.
    """
    contador = 0
    categoria_limpia = categoria.strip().upper()
    for prod in matriz:
        if str(prod[2]).strip().upper() == categoria_limpia:
            contador += 1
    return contador


def calcular_valor_total_inventario(matriz):
    """
    Calcula el valor económico total del inventario acumulando (precio * stock) de cada producto.
    
    Parámetros:
        matriz (list): Matriz de productos.
        
    Retorna:
        float: Valor monetario total del inventario.
    """
    total = 0.0
    for prod in matriz:
        precio = prod[3]
        stock = prod[4]
        total += precio * stock
    return total


def calcular_precio_promedio(matriz):
    """
    Calcula el precio promedio unitario de los productos en inventario.
    
    Parámetros:
        matriz (list): Matriz de productos.
        
    Retorna:
        float: Promedio de precios, o 0.0 si la matriz está vacía.
    """
    if len(matriz) == 0:
        return 0.0
    suma_precios = 0.0
    for prod in matriz:
        suma_precios += prod[3]
    return suma_precios / len(matriz)


def obtener_producto_mayor_precio(matriz):
    """
    Determina el producto con el mayor precio unitario en el inventario.
    
    Parámetros:
        matriz (list): Matriz de productos.
        
    Retorna:
        list: Fila del producto con mayor precio, o None si no hay registros.
    """
    if len(matriz) == 0:
        return None
    mayor = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][3] > mayor[3]:
            mayor = matriz[i]
    return mayor


def obtener_producto_menor_stock(matriz):
    """
    Determina el producto con menor cantidad de stock disponible (crítico para reposición).
    
    Parámetros:
        matriz (list): Matriz de productos.
        
    Retorna:
        list: Fila del producto con menor stock, o None si no hay registros.
    """
    if len(matriz) == 0:
        return None
    menor = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][4] < menor[4]:
            menor = matriz[i]
    return menor


def mostrar_panel_estadisticas(matriz, categorias):
    """
    Muestra en pantalla el informe estadístico consolidado del sistema.
    
    Parámetros:
        matriz (list): Matriz de productos.
        categorias (list): Lista de categorías válidas.
    """
    print("\n" + "=" * 60)
    print("           PANEL DE PROCESAMIENTO ESTADÍSTICO")
    print("=" * 60)

    total_registros = calcular_total_registros(matriz)

    if total_registros == 0:
        print(">> No hay registros suficientes para calcular estadísticas.")
        print("=" * 60)
        return

    # 1. Total general de registros
    print(f"1. Cantidad total de productos en inventario: {total_registros}")

    # 2. Cantidad de registros por categoría determinada (se consulta al usuario o se lista)
    print("\n2. Cantidad de productos por categoría:")
    for cat in categorias:
        cant_cat = contar_registros_por_categoria(matriz, cat)
        print(f"   - {cat:<15}: {cant_cat} producto(s)")

    # 3. Estadísticas adicionales de la temática
    valor_total = calcular_valor_total_inventario(matriz)
    precio_promedio = calcular_precio_promedio(matriz)
    prod_mas_caro = obtener_producto_mayor_precio(matriz)
    prod_menos_stock = obtener_producto_menor_stock(matriz)

    print("\n3. Métricas adicionales del inventario:")
    print(f"   - Valor monetario total del inventario: ${valor_total:,.2f}")
    print(f"   - Precio unitario promedio:              ${precio_promedio:.2f}")

    if prod_mas_caro is not None:
        print(f"   - Producto más costoso:                  [{prod_mas_caro[0]}] {prod_mas_caro[1]} (${prod_mas_caro[3]:.2f})")
    
    if prod_menos_stock is not None:
        print(f"   - Producto con menor stock (reposición): [{prod_menos_stock[0]}] {prod_menos_stock[1]} ({prod_menos_stock[4]} unidades)")

    print("=" * 60)
