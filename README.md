# Actividad Obligatoria 01 - Programación 1

## Información Académica
- Institución: Universidad Argentina de la Empresa (UADE)
- Facultad: Facultad de Ingeniería (FAIN)
- Departamento: Tecnología Informática Ciclo Inicial (DEINI)
- Materia: Programación 1 (Código 16263)
- Docente: Lic. Juan Pablo Nardone
- Cuatrimestre: Segundo Cuatrimestre 2026
- Fecha límite de entrega: Miércoles 9 de septiembre de 2026

### Integrantes del Grupo
- Bianca Freccia - Legajo: 1206377
- Lara Magalí Fodino - Legajo: 1216143
- Patricio Raber - Legajo: 1234652
- Agustina Cruz - Legajo: 1241748

---

## Temática Seleccionada: 1. Gestión de Inventario

El programa administra un inventario de productos comerciales utilizando una matriz (lista de listas), donde cada fila representa un producto y las columnas representan sus atributos.

### Estructura de Datos (Columnas de la Matriz)
- Columna 0 - Código: Identificador único del producto (ejemplo: P101).
- Columna 1 - Nombre: Descripción o nombre del producto (ejemplo: Arroz Largo Fino 1kg).
- Columna 2 - Tipo de producto: Categoría seleccionada entre un conjunto predefinido (Alimentos, Bebidas, Limpieza, Lácteos, Golosinas).
- Columna 3 - Precio: Valor numérico decimal positivo mayor a cero.
- Columna 4 - Stock disponible: Cantidad de unidades, número entero mayor o igual a cero.

### Datos Iniciales
El sistema inicia con 6 productos precargados (hardcodeados) en la matriz para permitir probar todas las funcionalidades desde el inicio.

---

## Funcionalidades del Menú
1. Dar de alta un registro: Permite ingresar un nuevo producto validando que el código identificador no esté repetido.
2. Consultar un registro: Busca un producto por su código y muestra todos sus datos en pantalla.
3. Modificar un registro: Localiza el producto por código y permite modificar uno o más de sus campos (nombre, categoría, precio o stock).
4. Eliminar un registro: Localiza el producto por código, solicita confirmación y lo elimina de la matriz.
5. Mostrar todos los registros: Imprime un listado completo en formato tabular alineado con encabezados.
6. Consultar registros por categoría: Permite elegir una categoría y muestra todos los productos que pertenecen a ella.
7. Realizar un procesamiento estadístico:
   - Cantidad total de registros almacenados.
   - Cantidad de registros por cada categoría.
   - Estadísticas adicionales: valor total acumulado del inventario, precio promedio, producto más caro y producto con menor stock (alerta de reposición).
8. Salir: Finaliza la ejecución del sistema.

---

## Validaciones Implementadas
- Control de códigos únicos (no repetidos).
- Opciones válidas en el menú principal y submenús.
- Pertenencia obligatoria a las categorías definidas.
- Control de tipos numéricos: enteros no negativos para stock y decimales mayores a cero para precio.
- Control de cadenas de texto no vacías.

---

## Modularización y Estructura del Código
El proyecto está dividido en módulos con separación clara de responsabilidades:
- principal.py: Inicializa la matriz con los registros hardcodeados y coordina el menú principal.
- menu.py: Contiene la presentación visual del menú y pausas de pantalla.
- crud.py: Contiene las funciones de Alta, Baja, Modificación, Consulta, Listado general y Consulta por categoría.
- estadisticas.py: Contiene las funciones de procesamiento estadístico y cálculos matemáticos.
- validaciones.py: Contiene las funciones de validación de datos ingresados por el usuario.

Nota de diseño: Todas las funciones reciben la matriz o listas por parámetro y retornan valores cuando corresponde, sin utilizar variables globales.

---

## Instrucciones de Ejecución
1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

python principal.py
