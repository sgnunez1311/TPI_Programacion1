# TPI_Programacion1

Explicacion del programa:
---------------------------
Es una aplicación de consola para gestionar un catálogo de países guardado en paises.csv. El archivo CSV funciona como base de datos y tiene cuatro
columnas:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
...


Actualmente contiene 10 países: Argentina, Japón, Brasil, Alemania, Francia, Australia, Canadá, Egipto, India y México.

La responsabilidad de cada archivo es:

TPI_paises.py (el "main"): Lee el CSV una vez al arrancar, muestra el menú y redirige cada opción a la función correspondiente de funciones.py.
Se repite hasta que el usuario elige salir.

funciones.py: Contiene toda la lógica: validación de entradas, lectura/escritura del CSV, alta, modificación, búsqueda, filtros, orden y estadísticas.

paises.csv: Persistencia de los datos. Se lee al inicio y se sobrescribe al modificar o se agrega una fila al dar de alta.

Instrucciones de uso: 
---------------------------
1 — Agregar: pide nombre, población, superficie y continente. Agrega una fila al final del CSV (modo "a"). No confirma por pantalla.

2 — Actualizar: pide el nombre, y si lo encuentra, reemplaza población y superficie (nombre y continente no se cambian). Reescribe todo el CSV con su cabecera.

3 — Buscar: busca coincidencias parciales e ignora mayúsculas/minúsculas. Relee el CSV en cada llamada.

4 — Filtrar: submenú con continente, rango de población o rango de superficie. En los rangos primero se pide el número mayor y después el menor.

5 — Ordenar: por nombre, por población (ascendente) o por superficie (elige ascendente/descendente). El orden cambia solo en memoria, no se guarda en el CSV.

6 — Estadísticas: submenú con mayor/menor población, promedios y cantidad por continente.

7 — Salir: termina el programa

Nota sobre la entrada: Los países y continentes del CSV están sin tildes (Japon, America, Africa, Oceania). Conviene escribirlos así.

Ejemplos de entradas y salida:
---------------------------
Ejemplo 1: buscar un país (opción 3)

¿Que desea hacer? 3

Ingrese un pais a buscar:
arg

{'nombre': 'Argentina', 'poblacion': '45376763', 'superficie': '2780400', 'continente': 'America'}


Ejemplo 2: filtrar por continente (opción 4 → 1)

¿Que desea hacer? 4

1. Filtrar por continente.
2. Rango de poblacion.
3. Rango de superficie.
¿Que desea hacer? 1

Ingrese el continente:
america

{'nombre': 'Argentina', 'poblacion': '45376763', 'superficie': '2780400', 'continente': 'America'}
{'nombre': 'Brasil', 'poblacion': '213993437', 'superficie': '8515767', 'continente': 'America'}
{'nombre': 'Canada', 'poblacion': '40097761', 'superficie': '9984670', 'continente': 'America'}
{'nombre': 'Mexico', 'poblacion': '130861007', 'superficie': '1964375', 'continente': 'America'}


Ejemplo 3: filtrar por rango de población (opción 4 → 2)

¿Que desea hacer? 4
1. Filtrar por continente.
2. Rango de poblacion.
3. Rango de superficie.
¿Que desea hacer? 2

Ingrese el rango de poblacion a buscar
Ingrese el numero mayor del rango
100000000

Ingrese el numero menor del rango
40000000

{'nombre': 'Argentina', 'poblacion': '45376763', 'superficie': '2780400', 'continente': 'America'}
{'nombre': 'Alemania', 'poblacion': '83149300', 'superficie': '357022', 'continente': 'Europa'}
{'nombre': 'Francia', 'poblacion': '68042591', 'superficie': '551695', 'continente': 'Europa'}
{'nombre': 'Canada', 'poblacion': '40097761', 'superficie': '9984670', 'continente': 'America'}


Ejemplo 4: ordenar por población (opción 5 → 2)

¿Que desea hacer? 5
1. Ordenar por nombre.
2. Ordenar por poblacion.
3. Superficie
¿Que desea hacer? 2

{'nombre': 'Australia', ...}
{'nombre': 'Canada', ...}
{'nombre': 'Argentina', ...}
{'nombre': 'Francia', ...}
{'nombre': 'Alemania', ...}
{'nombre': 'Egipto', ...}
{'nombre': 'Japon', ...}
{'nombre': 'Mexico', ...}
{'nombre': 'Brasil', ...}
{'nombre': 'India', ...}
(El ... es solo para abreviar: en pantalla se imprimen los diccionarios completos)


Ejemplo 5: estadísticas (opción 6 → 1 y → 2)

¿Que desea hacer? 6
1. Pais con mayor y menor poblacion.
2. Promedio de poblacion.
3. Promedio de superficie.
4. Cantidad de paises por continente.
¿Que desea hacer? 1

El pais con mayor poblacion es: India con: 1450935791
El pais con menor poblacion es: Australia con: 26770000

¿Que desea hacer? 6
Error. Ingrese una opcion del 1 al 3

¿Que desea hacer? 2

El promedio de poblacion en todos los paises es de: 230156490.8


Ejemplo 6: agregar un país (opción 1)

¿Que desea hacer? 1
Ingrese un pais para agregar:
Chile

Ingrese la poblacion:
19000000

Ingrese la superficie:
756096

Ingrese el continente:
America

Se agrego exitosamente: Chile,19000000,756096,America


Ejemplo 7: actualizar un país (opción 2)

¿Que desea hacer? 2

¿Que pais desea modificar?
Japon

Ingrese la nueva poblacion:
126000000

Ingrese la nueva superficie:
378000

Ha sido modificado con exito: Japon,126000000,378000,Asia

Si el nombre no se encuentra, imprime: Pais no encontrado.

---------------------------
Participacion de los integrantes:

Santino: Crear la logica de los archivos funciones.py, TPI_paises.py  y organizar el archivo paises.csv. Tambien toda la informacion en README.md y comentar el codigo.

Juan: Crear la documentación Académica y Técnica con la informacion de todos los conceptos usados en el programa y de agregarle la API.

Dionel: Encargado de la robustez del codigo, asegurando el correcto funcionamiento del mismo y manejando eficientemente los errores y comentar el codigo.