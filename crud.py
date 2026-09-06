"""
Módulo: crud.py
Descripción: Contiene las operaciones de gestión sobre la matriz de productos:
Alta, Consulta, Modificación, Eliminación, Listado general y Filtrado por categoría.
Materia: Programación 1 - FAIN UADE
"""

import validaciones


def buscar_indice_producto(matriz, codigo):
    """
    Busca un producto por su código en la matriz.
    
    Retorna:
        int: Índice de la fila donde se encuentra el producto, o -1 si no existe.
    """
    indice = 0
    encontrado = False

    while indice < len(matriz) and not encontrado:
        if matriz[indice][0] == codigo:
            encontrado = True
        else:
            indice += 1
    if not encontrado:
        indice = -1
    return indice


def alta_registro(matriz, categorias):
    """
    Permite registrar un nuevo producto en el sistema, validando todos sus campos
    y garantizando que el código no se encuentre duplicado.
    
    Parámetros:
        matriz (list): Matriz donde se almacenará el nuevo producto.
        categorias (list): Lista de categorías válidas.
    """
    print()
    print("=" * 50)
    print("           ALTA DE NUEVO PRODUCTO")
    print("=" * 50)

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto: ")

    if validaciones.validar_codigo_unico(codigo, matriz):
        print(">> Error: Ya existe un producto registrado con el código", codigo, ". Operación cancelada.")
        return

    nombre = validaciones.validar_texto_no_vacio("Ingrese el nombre del producto: ")
    categoria = validaciones.seleccionar_categoria(categorias)
    precio = validaciones.validar_flotante("Ingrese el precio unitario ($): ", 0.01)
    stock = validaciones.validar_entero("Ingrese el stock disponible: ", 0)

    nuevo_producto = [codigo, nombre, categoria, precio, stock]
    matriz.append(nuevo_producto)

    print()
    print(">> ¡Producto agregado exitosamente!")
    print("   Código:", codigo, "| Nombre:", nombre, "| Categoría:", categoria, "| Precio: $", precio, "| Stock:", stock)


def consultar_registro(matriz):
    """
    Permite consultar y visualizar todos los datos de un producto específico mediante su código.
    
    Parámetros:
        matriz (list): Matriz de productos.
    """
    print()
    print("=" * 50)
    print("           CONSULTA DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a consultar: ")
    indice = buscar_indice_producto(matriz, codigo)

    if indice != -1:
        prod = matriz[indice]
        print()
        print("-" * 40)
        print("         DETALLE DEL PRODUCTO")
        print("-" * 40)
        print("  Código:    ", prod[0])
        print("  Nombre:    ", prod[1])
        print("  Categoría: ", prod[2])
        print("  Precio:    $", prod[3])
        print("  Stock:     ", prod[4], "unidades")
        print("  Valor Total: $", prod[3] * prod[4])
        print("-" * 40)
    else:
        print()
        print(">> No se encontró ningún producto con el código", codigo)


def modificar_registro(matriz, categorias):
    """
    Permite modificar uno o más datos de un producto existente localizado por su código.
    
    Parámetros:
        matriz (list): Matriz de productos.
        categorias (list): Lista de categorías válidas.
    """
    print()
    print("=" * 50)
    print("         MODIFICACIÓN DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a modificar: ")
    indice = buscar_indice_producto(matriz, codigo)

    if indice == -1:
        print(">> No se encontró ningún producto con el código", codigo)
        return

    prod = matriz[indice]
    continuar = True

    while continuar:
        print()
        print("-" * 40)
        print("Modificando producto: [", prod[0], "] ", prod[1])
        print("1. Nombre actual: ", prod[1])
        print("2. Categoría actual: ", prod[2])
        print("3. Precio actual: $", prod[3])
        print("4. Stock actual: ", prod[4], "unidades")
        print("5. Volver al menú principal")
        print("-" * 40)

        opcion = validaciones.validar_opcion_menu(1, 5)

        if opcion == 1:
            nuevo_nombre = validaciones.validar_texto_no_vacio("Ingrese el nuevo nombre: ")
            prod[1] = nuevo_nombre
            print(">> Nombre actualizado correctamente.")
        elif opcion == 2:
            nueva_cat = validaciones.seleccionar_categoria(categorias)
            prod[2] = nueva_cat
            print(">> Categoría actualizada correctamente.")
        elif opcion == 3:
            nuevo_precio = validaciones.validar_flotante("Ingrese el nuevo precio ($): ", 0.01)
            prod[3] = nuevo_precio
            print(">> Precio actualizado correctamente.")
        elif opcion == 4:
            nuevo_stock = validaciones.validar_entero("Ingrese el nuevo stock: ", 0)
            prod[4] = nuevo_stock
            print(">> Stock actualizado correctamente.")
        elif opcion == 5:
            continuar = False
            print(">> Modificaciones guardadas.")


def eliminar_registro(matriz):
    """
    Permite eliminar un producto de la matriz luego de solicitar confirmación al usuario.
    
    Parámetros:
        matriz (list): Matriz de productos.
    """
    print()
    print("=" * 50)
    print("          ELIMINACIÓN DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a eliminar: ")
    indice = buscar_indice_producto(matriz, codigo)

    if indice == -1:
        print()
        print(">> No se encontró ningún producto con el código", codigo)
        return

    prod = matriz[indice]
    print()
    print("Producto encontrado:", prod[0], prod[1], "- Categoría:", prod[2], "- Precio: $", prod[3], "- Stock:", prod[4])

    confirmacion = validaciones.validar_texto_no_vacio("¿Está seguro de que desea eliminar este producto? (S/N): ").upper()

    if confirmacion == "S" or confirmacion == "s" or confirmacion == "SI" or confirmacion == "si":
        matriz.pop(indice)
        print()
        print(">> El producto con código", codigo, "ha sido eliminado exitosamente.")
    else:
        print()
        print(">> Operación cancelada. El producto no fue eliminado.")

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
