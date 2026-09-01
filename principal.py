"""
Programa: principal.py
Descripción: Módulo principal coordinador del sistema de Gestión de Inventario.
Inicia las estructuras de datos y gestiona el flujo del programa.
Materia: Programación 1 - FAIN UADE
Actividad Obligatoria 01
"""

import crud
import estadisticas
import menu


def inicializar_datos():
    """
    Inicializa y retorna la estructura de datos con al menos 5 registros
    cargados previamente (hardcodeados) y la lista de categorías definidas.
    
    Retorna:
        tuple: (matriz_productos, lista_categorias)
    """
    # Categorías predefinidas del sistema
    categorias = ["Alimentos", "Bebidas", "Limpieza", "Lácteos", "Golosinas"]

    # Matriz inicial con 6 registros hardcodeados para pruebas iniciales
    # Columnas: [0: Código, 1: Nombre, 2: Categoría, 3: Precio, 4: Stock]
    matriz_productos = [
        ["P101", "Arroz Largo Fino 1kg", "Alimentos", 1850.50, 40],
        ["P102", "Aceite de Girasol 1.5L", "Alimentos", 3200.00, 25],
        ["P103", "Gaseosa Cola 2.25L", "Bebidas", 2600.00, 50],
        ["P104", "Detergente Lavavajilla 750ml", "Limpieza", 1950.00, 15],
        ["P105", "Leche Entera 1L", "Lácteos", 1400.00, 60],
        ["P106", "Chocolate con Leche 100g", "Golosinas", 2100.00, 8]
    ]

    return matriz_productos, categorias


def main():
    """
    Función principal que coordina el ciclo de vida del sistema,
    llamando a las distintas funcionalidades según la opción elegida por el usuario.
    """
    matriz_productos, categorias = inicializar_datos()
    ejecutando = True

    while ejecutando:
        menu.mostrar_menu_principal()
        opcion = menu.pedir_opcion_menu_principal()

        if opcion == 1:
            crud.alta_registro(matriz_productos, categorias)
            menu.pausar()

        elif opcion == 2:
            crud.consultar_registro(matriz_productos)
            menu.pausar()

        elif opcion == 3:
            crud.modificar_registro(matriz_productos, categorias)
            menu.pausar()

        elif opcion == 4:
            crud.eliminar_registro(matriz_productos)
            menu.pausar()

        elif opcion == 5:
            crud.mostrar_todos_los_registros(matriz_productos)
            menu.pausar()

        elif opcion == 6:
            crud.consultar_por_categoria(matriz_productos, categorias)
            menu.pausar()

        elif opcion == 7:
            estadisticas.mostrar_panel_estadisticas(matriz_productos, categorias)
            menu.pausar()

        elif opcion == 8:
            print("\n" + "=" * 55)
            print("  ¡Gracias por utilizar el Sistema de Inventario!")
            print("                 Programa finalizado.")
            print("=" * 55 + "\n")
            ejecutando = False


if __name__ == "__main__":
    main()
