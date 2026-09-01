"""
Módulo: menu.py
Descripción: Contiene las funciones encargadas de mostrar los menús de navegación
y gestionar la interacción visual con el usuario por consola.
Materia: Programación 1 - FAIN UADE
"""

import validaciones


def mostrar_menu_principal():
    """
    Imprime en pantalla las opciones del menú principal del sistema.
    """
    print("\n" + "=" * 55)
    print("      SISTEMA DE GESTIÓN DE INVENTARIO - UADE P1")
    print("=" * 55)
    print("  [1] Dar de alta un producto")
    print("  [2] Consultar un producto por código")
    print("  [3] Modificar un producto")
    print("  [4] Eliminar un producto")
    print("  [5] Mostrar todos los productos (Listado general)")
    print("  [6] Consultar productos por categoría")
    print("  [7] Procesamiento estadístico del inventario")
    print("  [8] Salir del sistema")
    print("=" * 55)


def pedir_opcion_menu_principal():
    """
    Solicita y valida que la opción ingresada por el usuario corresponda a una opción del menú.
    
    Retorna:
        int: Número de opción seleccionada (entre 1 y 8).
    """
    return validaciones.validar_opcion_menu(1, 8)


def pausar():
    """
    Realiza una pausa en la ejecución para que el usuario pueda leer los resultados antes de continuar.
    """
    input("\nPresione [ENTER] para continuar...")
