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
    
    Parámetros:
        matriz (list): Matriz de productos.
        codigo (str): Código identificador a buscar.
        
    Retorna:
        int: Índice de la fila donde se encuentra el producto, o -1 si no existe.
    """
    codigo_buscado = codigo.strip().upper()
    for i in range(len(matriz)):
        if str(matriz[i][0]).strip().upper() == codigo_buscado:
            return i
    return -1


def alta_registro(matriz, categorias):
    """
    Permite registrar un nuevo producto en el sistema, validando todos sus campos
    y garantizando que el código no se encuentre duplicado.
    
    Parámetros:
        matriz (list): Matriz donde se almacenará el nuevo producto.
        categorias (list): Lista de categorías válidas.
    """
    print("\n" + "=" * 50)
    print("           ALTA DE NUEVO PRODUCTO")
    print("=" * 50)

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto: ").upper()

    if validaciones.validar_codigo_unico(codigo, matriz):
        print(f"\n>> Error: Ya existe un producto registrado con el código '{codigo}'. Operación cancelada.")
        return

    nombre = validaciones.validar_texto_no_vacio("Ingrese el nombre del producto: ")
    categoria = validaciones.seleccionar_categoria(categorias)
    precio = validaciones.validar_flotante("Ingrese el precio unitario ($): ", minimo=0.01)
    stock = validaciones.validar_entero("Ingrese el stock disponible: ", minimo=0)

    nuevo_producto = [codigo, nombre, categoria, precio, stock]
    matriz.append(nuevo_producto)

    print("\n>> ¡Producto agregado exitosamente!")
    print(f"   Código: {codigo} | Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio:.2f} | Stock: {stock}")


def consultar_registro(matriz):
    """
    Permite consultar y visualizar todos los datos de un producto específico mediante su código.
    
    Parámetros:
        matriz (list): Matriz de productos.
    """
    print("\n" + "=" * 50)
    print("           CONSULTA DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a consultar: ").upper()
    indice = buscar_indice_producto(matriz, codigo)

    if indice != -1:
        prod = matriz[indice]
        print("\n" + "-" * 40)
        print("         DETALLE DEL PRODUCTO")
        print("-" * 40)
        print(f"  Código:     {prod[0]}")
        print(f"  Nombre:     {prod[1]}")
        print(f"  Categoría:  {prod[2]}")
        print(f"  Precio:     ${prod[3]:.2f}")
        print(f"  Stock:      {prod[4]} unidades")
        print(f"  Valor Total:${prod[3] * prod[4]:.2f}")
        print("-" * 40)
    else:
        print(f"\n>> No se encontró ningún producto con el código '{codigo}'.")


def modificar_registro(matriz, categorias):
    """
    Permite modificar uno o más datos de un producto existente localizado por su código.
    
    Parámetros:
        matriz (list): Matriz de productos.
        categorias (list): Lista de categorías válidas.
    """
    print("\n" + "=" * 50)
    print("         MODIFICACIÓN DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a modificar: ").upper()
    indice = buscar_indice_producto(matriz, codigo)

    if indice == -1:
        print(f"\n>> No se encontró ningún producto con el código '{codigo}'.")
        return

    prod = matriz[indice]
    continuar = True

    while continuar:
        print("\n" + "-" * 40)
        print(f"Modificando producto: [{prod[0]}] {prod[1]}")
        print(f"1. Nombre actual: {prod[1]}")
        print(f"2. Categoría actual: {prod[2]}")
        print(f"3. Precio actual: ${prod[3]:.2f}")
        print(f"4. Stock actual: {prod[4]} unidades")
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
            nuevo_precio = validaciones.validar_flotante("Ingrese el nuevo precio ($): ", minimo=0.01)
            prod[3] = nuevo_precio
            print(">> Precio actualizado correctamente.")
        elif opcion == 4:
            nuevo_stock = validaciones.validar_entero("Ingrese el nuevo stock: ", minimo=0)
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
    print("\n" + "=" * 50)
    print("          ELIMINACIÓN DE PRODUCTO")
    print("=" * 50)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    codigo = validaciones.validar_texto_no_vacio("Ingrese el código del producto a eliminar: ").upper()
    indice = buscar_indice_producto(matriz, codigo)

    if indice == -1:
        print(f"\n>> No se encontró ningún producto con el código '{codigo}'.")
        return

    prod = matriz[indice]
    print(f"\nProducto encontrado: [{prod[0]}] {prod[1]} - Categoría: {prod[2]} - Precio: ${prod[3]:.2f} - Stock: {prod[4]}")
    
    confirmacion = validaciones.validar_texto_no_vacio("¿Está seguro de que desea eliminar este producto? (S/N): ").upper()

    if confirmacion == "S" or confirmacion == "SI":
        matriz.pop(indice)
        print(f"\n>> El producto con código '{codigo}' ha sido eliminado exitosamente.")
    else:
        print("\n>> Operación cancelada. El producto no fue eliminado.")


def mostrar_todos_los_registros(matriz):
    """
    Imprime un listado completo de los productos en formato tabular con columnas alineadas.
    
    Parámetros:
        matriz (list): Matriz de productos.
    """
    print("\n" + "=" * 80)
    print("                    LISTADO GENERAL DE INVENTARIO")
    print("=" * 80)

    if len(matriz) == 0:
        print(">> No hay productos para mostrar en el inventario.")
        print("=" * 80)
        return

    # Encabezados con alineación
    print(f"{'CÓDIGO':<10} | {'NOMBRE':<30} | {'CATEGORÍA':<15} | {'PRECIO':>10} | {'STOCK':>6}")
    print("-" * 80)

    for prod in matriz:
        cod = str(prod[0])
        nom = str(prod[1])
        cat = str(prod[2])
        prec = f"${prod[3]:.2f}"
        stk = str(prod[4])
        print(f"{cod:<10} | {nom:<30} | {cat:<15} | {prec:>10} | {stk:>6}")

    print("=" * 80)
    print(f"Total de productos en lista: {len(matriz)}")


def consultar_por_categoria(matriz, categorias):
    """
    Permite seleccionar una categoría y muestra todos los productos pertenecientes a la misma.
    
    Parámetros:
        matriz (list): Matriz de productos.
        categorias (list): Lista de categorías válidas.
    """
    print("\n" + "=" * 80)
    print("             CONSULTA DE PRODUCTOS POR CATEGORÍA")
    print("=" * 80)

    if len(matriz) == 0:
        print(">> No hay productos registrados en el sistema.")
        return

    categoria_seleccionada = validaciones.seleccionar_categoria(categorias)

    print("\n" + "=" * 80)
    print(f"               PRODUCTOS EN LA CATEGORÍA: {categoria_seleccionada.upper()}")
    print("=" * 80)
    print(f"{'CÓDIGO':<10} | {'NOMBRE':<30} | {'CATEGORÍA':<15} | {'PRECIO':>10} | {'STOCK':>6}")
    print("-" * 80)

    encontrados = 0
    for prod in matriz:
        if str(prod[2]).strip().upper() == categoria_seleccionada.strip().upper():
            cod = str(prod[0])
            nom = str(prod[1])
            cat = str(prod[2])
            prec = f"${prod[3]:.2f}"
            stk = str(prod[4])
            print(f"{cod:<10} | {nom:<30} | {cat:<15} | {prec:>10} | {stk:>6}")
            encontrados += 1

    print("=" * 80)
    if encontrados == 0:
        print(f">> No se encontraron productos registrados en la categoría '{categoria_seleccionada}'.")
    else:
        print(f"Total de productos encontrados en '{categoria_seleccionada}': {encontrados}")
