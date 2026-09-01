# Actividad Obligatoria 01 - Programacion 1

## Informacion Academica
- Institucion: Universidad Argentina de la Empresa (UADE)
- Facultad: Facultad de Ingenieria (FAIN)
- Departamento: Tecnologia Informatica Ciclo Inicial (DEINI)
- Materia: Programacion 1 (Codigo 16263)
- Docente: Lic. Juan Pablo Nardone
- Cuatrimestre: Segundo Cuatrimestre 2026
- Fecha limite de entrega: Miercoles 9 de septiembre de 2026

### Integrantes del Grupo
- Bianca Freccia - Legajo: 1206377
- Lara Magali Fodino - Legajo: 1216143
- Patricio Raber - Legajo: 1234652
- Agustina Cruz - Legajo: 1241748

---

## Tematica Seleccionada: 1. Gestión de Inventario

El programa administra un inventario de productos comerciales utilizando una matriz (lista de listas), donde cada fila representa un producto y las columnas representan sus atributos.

### Estructura de Datos (Columnas de la Matriz)
- Columna 0 - Codigo: Identificador unico del producto (ejemplo: P101).
- Columna 1 - Nombre: Descripcion o nombre del producto (ejemplo: Arroz Largo Fino 1kg).
- Columna 2 - Tipo de producto: Categoria seleccionada entre un conjunto predefinido (Alimentos, Bebidas, Limpieza, Lacteos, Golosinas).
- Columna 3 - Precio: Valor numerico decimal positivo mayor a cero.
- Columna 4 - Stock disponible: Cantidad de unidades, numero entero mayor o igual a cero.

### Datos Iniciales
El sistema inicia con 6 productos precargados (hardcodeados) en la matriz para permitir probar todas las funcionalidades desde el inicio.

---

## Funcionalidades del Menú
1. Dar de alta un registro: Permite ingresar un nuevo producto validando que el codigo identificador no este repetido.
2. Consultar un registro: Busca un producto por su codigo y muestra todos sus datos en pantalla.
3. Modificar un registro: Localiza el producto por codigo y permite modificar uno o mas de sus campos (nombre, categoria, precio o stock).
4. Eliminar un registro: Localiza el producto por codigo, solicita confirmacion y lo elimina de la matriz.
5. Mostrar todos los registros: Imprime un listado completo en formato tabular alineado con encabezados.
6. Consultar registros por categoria: Permite elegir una categoria y muestra todos los productos que pertenecen a ella.
7. Realizar un procesamiento estadistico:
   - Cantidad total de registros almacenados.
   - Cantidad de registros por cada categoria.
   - Estadisticas adicionales: valor total acumulado del inventario, precio promedio, producto mas caro y producto con menor stock (alerta de reposicion).
8. Salir: Finaliza la ejecucion del sistema.

---

## Validaciones Implementadas
- Control de codigos unicos (no repetidos).
- Opciones validas en el menu principal y submenus.
- Pertenencia obligatoria a las categorias definidas.
- Control de tipos numericos: enteros no negativos para stock y decimales mayores a cero para precio.
- Control de cadenas de texto no vacias.

---

## Modularización y Estructura del Código
El proyecto esta dividido en modulos con separacion clara de responsabilidades:
- principal.py: Inicializa la matriz con los registros hardcodeados y coordina el menu principal.
- menu.py: Contiene la presentacion visual del menu y pausas de pantalla.
- crud.py: Contiene las funciones de Alta, Baja, Modificacion, Consulta, Listado general y Consulta por categoria.
- estadisticas.py: Contiene las funciones de procesamiento estadistico y calculos matematicos.
- validaciones.py: Contiene las funciones de validacion de datos ingresados por el usuario.

Nota de diseno: Todas las funciones reciben la matriz o listas por parametro y retornan valores cuando corresponde, sin utilizar variables globales.

---

## Instrucciones de Ejecución
1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

python principal.py
