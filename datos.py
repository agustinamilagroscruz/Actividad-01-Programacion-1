"""
Módulo: datos.py
Descripción: Contiene los datos iniciales del sistema de Gestión de Inventario.
Materia: Programación 1 - FAIN UADE
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
