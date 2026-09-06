"""
Módulo: validaciones.py
Descripción: Contiene todas las funciones encargadas de validar datos ingresados
por el usuario para asegurar la integridad de la información en el sistema.
Materia: Programación 1 - FAIN UADE
"""


def validar_texto_no_vacio(mensaje):
    """
    Solicita un texto al usuario y asegura que no quede vacío.
    
    """
    texto = input(mensaje)
    while texto == "":
        print(">> Error: El campo no puede estar vacío. Intente nuevamente.")
        texto = input(mensaje)
    return texto


def validar_entero(mensaje, minimo):
    """
    Solicita un número entero y verifica que sea válido y mayor o igual al mínimo establecido.
    
    Parámetros:
        mensaje (str): Mensaje descriptivo para el usuario.
        minimo (int): Valor mínimo permitido.
        
    Retorna:
        int: El número entero validado.
    """
    print(mensaje, end="")
    numero = int(input())

    while numero < minimo:
        print(">> Error: El número debe ser mayor o igual a", minimo)
        print(mensaje, end="")
        numero = int(input())

    return numero


def validar_flotante(mensaje, minimo):
    """
    Solicita un número decimal (flotante) y verifica que sea mayor o igual al mínimo.
    
    Parámetros:
        mensaje (str): Mensaje descriptivo para el usuario.
        minimo (float): Valor mínimo permitido.
        
    Retorna:
        float: El número decimal validado.
    """
    print(mensaje, end="")
    numero = float(input())

    while numero < minimo:
        print(">> Error: El valor debe ser mayor o igual a", minimo)
        print(mensaje, end="")
        numero = float(input())

    return numero


def validar_codigo_unico(codigo, matriz):
    """
    Verifica si un código ya se encuentra registrado en la matriz.
    
    Parámetros:
        codigo (str): Código a comprobar.
        matriz (list): Matriz con los registros de productos.
        
    Retorna:
        bool: True si el código ya existe, False en caso contrario.
    """
    encontrado = False
    i = 0
    while i < len(matriz) and not encontrado:
        if matriz[i][0] == codigo:
            encontrado = True
        else:
            i += 1
    return encontrado


def seleccionar_categoria(categorias):
    """
    Muestra la lista de categorías disponibles numeradas y permite al usuario elegir una.
    
    Parámetros:
        categorias (list): Lista de nombres de categorías válidas.
        
    Retorna:
        str: El nombre de la categoría seleccionada.
    """
    print()
    print("Categorías disponibles:")
    for i in range(len(categorias)):
        print(i + 1, "-", categorias[i])
    opcion = validar_opcion_menu(1, len(categorias))
    return categorias[opcion - 1]


def validar_opcion_menu(opcion_min, opcion_max):
    """
    Solicita y valida la opción del menú principal.
    
    Parámetros:
        opcion_min (int): Opción numérica mínima válida.
        opcion_max (int): Opción numérica máxima válida.
        
    Retorna:
        int: La opción seleccionada válida.
    """
    print("Ingrese una opción entre", opcion_min, "y", opcion_max, end=": ")
    opcion = int(input())

    while opcion < opcion_min or opcion > opcion_max:
        print(">> Error: Opción fuera de rango. Debe ser entre", opcion_min, "y", opcion_max)
        print("Ingrese una opción entre", opcion_min, "y", opcion_max, end=": ")
        opcion = int(input())
    return opcion