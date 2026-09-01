"""
Módulo: validaciones.py
Descripción: Contiene todas las funciones encargadas de validar datos ingresados
por el usuario para asegurar la integridad de la información en el sistema.
Materia: Programación 1 - FAIN UADE
"""


def validar_texto_no_vacio(mensaje):
    """
    Solicita un texto al usuario y asegura que no quede vacío ni compuesto solo por espacios.
    
    Parámetros:
        mensaje (str): El mensaje que se muestra al solicitar el dato.
        
    Retorna:
        str: El texto ingresado sin espacios en los extremos.
    """
    texto = input(mensaje).strip()
    while len(texto) == 0:
        print(">> Error: El campo no puede estar vacío. Intente nuevamente.")
        texto = input(mensaje).strip()
    return texto


def validar_entero(mensaje, minimo=0):
    """
    Solicita un número entero y verifica que sea válido y mayor o igual al mínimo establecido.
    
    Parámetros:
        mensaje (str): Mensaje descriptivo para el usuario.
        minimo (int): Valor mínimo permitido (por defecto 0).
        
    Retorna:
        int: El número entero validado.
    """
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
            if numero >= minimo:
                valido = True
            else:
                print(f">> Error: El número debe ser mayor o igual a {minimo}.")
        except ValueError:
            print(">> Error: Debe ingresar un número entero válido.")
    return numero


def validar_flotante(mensaje, minimo=0.01):
    """
    Solicita un número decimal (flotante) y verifica que sea mayor o igual al mínimo.
    
    Parámetros:
        mensaje (str): Mensaje descriptivo para el usuario.
        minimo (float): Valor mínimo permitido (por defecto 0.01).
        
    Retorna:
        float: El número decimal validado.
    """
    valido = False
    numero = 0.0
    while not valido:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(entrada)
            if numero >= minimo:
                valido = True
            else:
                print(f">> Error: El valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print(">> Error: Debe ingresar un valor numérico válido (ejemplo: 1250.50).")
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
    codigo_limpio = codigo.strip().upper()
    for fila in matriz:
        if str(fila[0]).strip().upper() == codigo_limpio:
            return True
    return False


def seleccionar_categoria(categorias):
    """
    Muestra la lista de categorías disponibles numeradas y permite al usuario elegir una.
    
    Parámetros:
        categorias (list): Lista de nombres de categorías válidas.
        
    Retorna:
        str: El nombre de la categoría seleccionada.
    """
    print("\nCategorías disponibles:")
    for i in range(len(categorias)):
        print(f"  [{i + 1}] {categorias[i]}")
        
    opcion = validar_entero(f"Seleccione una categoría (1 - {len(categorias)}): ", minimo=1)
    while opcion > len(categorias):
        print(f">> Error: La opción debe estar entre 1 y {len(categorias)}.")
        opcion = validar_entero(f"Seleccione una categoría (1 - {len(categorias)}): ", minimo=1)
        
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
    opcion = validar_entero("Ingrese una opción: ", minimo=opcion_min)
    while opcion > opcion_max:
        print(f">> Error: Opción fuera de rango. Debe ser entre {opcion_min} y {opcion_max}.")
        opcion = validar_entero("Ingrese una opción: ", minimo=opcion_min)
    return opcion
