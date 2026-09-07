"""
Programa: principal.py
Descripción: Módulo principal coordinador del sistema de Gestión de Inventario.
Inicia las estructuras de datos y gestiona el flujo del programa.
Materia: Programación 1 - FAIN UADE
Actividad Obligatoria 01
"""

from datos import matriz_productos, categorias
from crud import alta_registro, consultar_registro, modificar_registro, eliminar_registro
from consultas import mostrar_todos_los_registros, consultar_por_categoria
from estadisticas import mostrar_panel_estadisticas
from menu import mostrar_menu_principal, pedir_opcion_menu_principal, pausar


"""
Se inicializan los datos y luego se coordinan las distintas funcionalidades según la opción elegida por el usuario.
"""
opcion = 0

while opcion != 8:
    mostrar_menu_principal()
    opcion = pedir_opcion_menu_principal()

    if opcion == 1:
        alta_registro(matriz_productos, categorias)
        pausar()
    elif opcion == 2:
        consultar_registro(matriz_productos)
        pausar()
    elif opcion == 3:
        modificar_registro(matriz_productos, categorias)
        pausar()
    elif opcion == 4:
        eliminar_registro(matriz_productos)
        pausar()
    elif opcion == 5:
        mostrar_todos_los_registros(matriz_productos)
        pausar()
    elif opcion == 6:
        consultar_por_categoria(matriz_productos, categorias)
        pausar()
    elif opcion == 7:
        mostrar_panel_estadisticas(matriz_productos, categorias)
        pausar()
    else:
        print()
        print("=" * 55)
        print("  ¡Gracias por utilizar el Sistema de Inventario!")
        print("                 Programa finalizado.")
        print("=" * 55)
