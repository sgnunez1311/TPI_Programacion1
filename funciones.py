import csv
import json
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

#Usado para pedir un numero, comprobar que sea uno correcto y devolverlo
def comprobar_num():
    while True:
        try:
            numero = int(input())
            if numero > 0:
                return numero
            else:
                print("Error. Ingrese un numero entero positivo.")
        except ValueError:
            print("Error. Ingrese un numero entero positivo.")
#Usado para comprobar una palabra, comprobar que sea correcta y devolverla
def comprobar_palabra():
    while True:
        palabra = input()
        if palabra.isalpha():
            return palabra
        else:
            print("Error. Ingrese una palabra usando letras.")
#Usado para escribir los datos del csv dentro del programa y guarardarlos para futuras modificaciones
def iniciar_csv():
    #creamos una lista vacia para guardar los paises en diccionarios del csv
    paises = []

    #Abrimos el archivo para leer la informacion que ya contiene
    try:
        with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:
            #guardamos la informacion en una variable
            lector = csv.DictReader(archivo)
            #leemos diccionario por diccionario y lo guardamos en la variable "fila"
            for fila in lector:
            #Agregamos cada diccionario por separado a la lista "paises"
                paises.append(fila)
            return paises
    except FileNotFoundError:
        print("Error. El archivo no se encontró.")
    except PermissionError:
        print("No tienes permiso para abrir este archivo.")
    except OSError:
        print("Error. Hubo un error en el sistema. Intente otra vez.")
#Usado para agregar un pais nuevo
def pais_nuevo(paises):
    #Preguntamos los datos del nuevo pais
    print("Ingrese un pais para agregar: ")
    pais = comprobar_palabra()
    
    print("Ingrese la poblacion: ")
    poblacion = comprobar_num()

    print("Ingrese la superficie: ")
    superficie = comprobar_num()

    print("Ingrese el continente: ")
    continente = comprobar_palabra()

    #guardamos los datos en un diccionario
    nuevo_pais = {"nombre": pais, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    guardar_pais_nuevo(paises, nuevo_pais)

#Usado para agregar un pais (ingresado a mano o consultado por API) al csv
def guardar_pais_nuevo(paises, nuevo_pais):
    #definimos las columnas
    columnas = ["nombre", "poblacion", "superficie", "continente"]

    #Guardamos el nuevo pais en la lista de paises
    paises.append(nuevo_pais)

    try:
        #Iniciamos el archivo en modo "a" para que se agregue la informacion y no borre todo
        with open("paises.csv", "a", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas, lineterminator="\n")
            escritor.writerow(nuevo_pais)
        print(f"Se agrego exitosamente: {nuevo_pais}")
        return True
    except PermissionError:
        print("No tienes permiso para abrir este archivo.")
    except OSError:
        print("Error. Hubo un error en el sistema. Intente otra vez.")
    return False
#Usado para actualizar la poblacion y la superficie de un pais
def modificar_pais(paises):
    columnas = ["nombre", "poblacion", "superficie", "continente"]
    print("¿Que pais desea modificar?")
    buscar_pais = comprobar_palabra()

    encontrado = False

    for pais in paises:
        if pais["nombre"].lower() == buscar_pais.lower():
            encontrado = True

            print("Ingrese la nueva poblacion: ")
            pais["poblacion"] = comprobar_num()
            print("Ingrese la nueva superficie: ")
            pais["superficie"] = comprobar_num()

    if encontrado:
        try:
            with open ("paises.csv", "w", encoding="utf-8", newline="") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=columnas)
                escritor.writeheader()
                escritor.writerows(paises)
                print(f"Ha sido modificado con exito: {pais}")
        except FileNotFoundError:
            print("Error. El archivo no se encontró.")
        except PermissionError:
            print("No tienes permiso para abrir este archivo.")
        except OSError:
            print("Error. Hubo un error en el sistema. Intente otra vez.")
    else:
        print("Pais no encontrado.")
#Busca un pais y lo muestra
def buscar_pais():
    print("Ingrese un pais a buscar: ")
    buscar = comprobar_palabra()
    try:
        with open("paises.csv","r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            encontrado = False
            for pais in lector:
                if buscar.lower() in pais["nombre"].lower():
                    print(pais)
                    encontrado = True
            if encontrado == False:
                print("Pais no encontrado.")
    except FileNotFoundError:
        print("Error. El archivo no se encontró.")
    except PermissionError:
        print("No tienes permiso para abrir este archivo.")
    except OSError:
        print("Error. Hubo un error en el sistema. Intente otra vez.")
#Abre un menu para filtrar paises con diferentes condiciones
def filtrar_paises(paises):
    print("1. Filtrar por continente.")
    print("2. Rango de poblacion.")
    print("3. Rango de superficie.")
    print("¿Que desea hacer?")
    caso = comprobar_num()

    match caso:
        case 1:
            print("Ingrese el continente: ")
            continente = comprobar_palabra()

            for pais in paises:
                if continente.capitalize() == pais["continente"]:
                    print(pais)


        case 2:
            print("Ingrese el rango de poblacion a buscar")
            print("Ingrese el numero mayor del rango")
            rango_mayor = comprobar_num()
            print("Ingrese el numero menor del rango")
            rango_menor = comprobar_num()

            for pais in paises:
                if int(pais["poblacion"]) <= rango_mayor and int(pais["poblacion"]) >= rango_menor:
                    print(pais)

        case 3:
            print("Ingrese el rango de superficie a buscar")
            print("Ingrese el numero mayor del rango")
            rango_mayor = comprobar_num()
            print("Ingrese el numero menor del rango")
            rango_menor = comprobar_num()

            for pais in paises:
                if int(pais["superficie"]) <= rango_mayor and int(pais["superficie"]) >= rango_menor:
                    print(pais)
        case _:
            print("Error. Ingrese una opcion del 1 al 3")
#Ordena los paises de diferentes maneras.
def ordenar_paises(paises):
    print("1. Ordenar por nombre.")
    print("2. Ordenar por poblacion.")
    print("3. Superficie")
    print("¿Que desea hacer?")
    caso = comprobar_num()

    match caso:
        case 1:
            paises.sort(key=lambda pais: pais["nombre"])

            for pais in paises:
                print(pais)

        case 2:
            paises.sort(key=lambda pais: int(pais["poblacion"]))

            for pais in paises:
                print(pais)

        case 3:
            print("Ordenar de manera:")
            print("1. Ascendente")
            print("2. Descendente")
            decision = comprobar_num()

            if decision == 1:
                paises.sort(key=lambda pais: int(pais["superficie"]))

            elif decision == 2:
                paises.sort(key=lambda pais: int(pais["superficie"]), reverse=True)

            for pais in paises:
                print(pais)
        case _:
            print("Error. Ingrese una opcion del 1 al 3")
#Muestra las estadisticas de los paises segun condiciones.
def estadisticas(paises):
    print("1. Pais con mayor y menor poblacion.")
    print("2. Promedio de poblacion.")
    print("3. Promedio de superficie.")
    print("4. Cantidad de paises por continente.")
    print("¿Que desea hacer?")

    caso = comprobar_num()

    match caso:
        case 1:
            mayor = 0
            pais_mayor = ""
            menor = int(paises[0]["poblacion"])
            
            pais_menor = ""
            try:
                with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:

                    lector = csv.DictReader(archivo)

                    for fila in lector:
                        if int(fila["poblacion"]) > mayor:
                            mayor = int(fila["poblacion"])
                            pais_mayor = fila["nombre"]
                        if int(fila["poblacion"]) < menor:
                            menor = int(fila["poblacion"])
                            pais_menor = fila["nombre"]
                    print(f"El pais con mayor poblacion es: {pais_mayor} con: {mayor}")
                    print(f"El pais con menor poblacion es: {pais_menor} con: {menor}")

            except FileNotFoundError:
                print("Error. El archivo no se encontró.")
            except PermissionError:
                print("No tienes permiso para abrir este archivo.")
            except OSError:
                print("Error. Hubo un error en el sistema. Intente otra vez.")

        case 2:
            suma = 0
            promedio = 0
            cantidad = len(paises)
            try:
                with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:

                    lector = csv.DictReader(archivo)

                    for fila in lector:
                        suma += int(fila["poblacion"])
                    promedio = suma / cantidad
                    promedio = round(promedio, 2)
                    print("El promedio de poblacion en todos los paises es de:",promedio)

            except FileNotFoundError:
                print("Error. El archivo no se encontró.")
            except PermissionError:
                print("No tienes permiso para abrir este archivo.")
            except OSError:
                print("Error. Hubo un error en el sistema. Intente otra vez.")

        case 3:
            suma = 0
            promedio = 0
            cantidad = len(paises)
            try:
                with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:

                    lector = csv.DictReader(archivo)

                    for fila in lector:
                        suma += int(fila["superficie"])
                    promedio = suma / cantidad
                    promedio = round(promedio, 2)
                    print("El promedio de superficie en todos los paises es de:",promedio)

            except FileNotFoundError:
                print("Error. El archivo no se encontró.")
            except PermissionError:
                print("No tienes permiso para abrir este archivo.")
            except OSError:
                print("Error. Hubo un error en el sistema. Intente otra vez.")

        case 4:
            america = 0
            africa = 0
            oceania = 0
            europa = 0
            asia = 0

            for continente in paises:
                if continente["continente"].lower() == "america":
                    america += 1
                elif continente["continente"].lower() == "africa":
                    africa += 1
                elif continente["continente"].lower() == "oceania":
                    oceania += 1
                elif continente["continente"].lower() == "europa":
                    europa += 1
                elif continente["continente"].lower() == "asia":
                    asia += 1
            print(f"America tiene {america} paises")
            print(f"Africa tiene {africa} paises")
            print(f"Oceania tiene {oceania} paises")
            print(f"Europa tiene {europa} paises")
            print(f"Asia tiene {asia} paises")
        case _:
            print("Opcion no encontrada. Elija un numero del 1-4.")

#Nombres en español (sin tildes) que usa el csv para los paises mas comunes
NOMBRES_API = {
    "alemania": "Alemania",
    "argentina": "Argentina",
    "australia": "Australia",
    "brasil": "Brasil",
    "brazil": "Brasil",
    "canada": "Canada",
    "china": "China",
    "corea del sur": "Corea del Sur",
    "egipto": "Egipto",
    "egypt": "Egipto",
    "estados unidos": "Estados Unidos",
    "francia": "Francia",
    "france": "Francia",
    "germany": "Alemania",
    "india": "India",
    "japon": "Japon",
    "japan": "Japon",
    "mexico": "Mexico",
    "reino unido": "Reino Unido",
    "south korea": "Corea del Sur",
    "united kingdom": "Reino Unido",
    "united states": "Estados Unidos"
}

#Nombres que espera la API cuando el usuario escribe el pais en español
NOMBRES_CONSULTA = {
    "alemania": "germany",
    "brasil": "brazil",
    "corea del sur": "south korea",
    "egipto": "egypt",
    "estados unidos": "united states",
    "francia": "france",
    "japon": "japan",
    "reino unido": "united kingdom"
}

#La API devuelve los continentes en ingles y en plural; el csv usa los nombres en español
CONTINENTES_API = {
    "america": "America",
    "americas": "America",
    "africa": "Africa",
    "asia": "Asia",
    "europa": "Europa",
    "europe": "Europa",
    "oceania": "Oceania"
}

#Quita las tildes sin cambiar el resto del texto
def sin_tildes(texto):
    texto = unicodedata.normalize("NFD", str(texto))
    return "".join(caracter for caracter in texto if unicodedata.category(caracter) != "Mn")

#Deja un texto en minusculas y sin tildes para poder compararlo
def normalizar_texto(texto):
    return sin_tildes(texto).strip().lower()

#Adapta la entrada del usuario a un nombre que la API pueda encontrar
def nombre_para_consulta(nombre):
    texto = normalizar_texto(nombre)
    return NOMBRES_CONSULTA.get(texto, texto)

#Devuelve el nombre con el formato que ya usa el csv (sin tildes)
def nombre_para_csv(nombre):
    texto = sin_tildes(nombre).strip()
    return NOMBRES_API.get(normalizar_texto(texto), texto)

#Comprueba si el pais ya esta en la lista, incluso si llega con otro nombre (Brazil/Brasil)
def pais_existe(paises, nombre):
    nombre_normalizado = normalizar_texto(nombre)
    nombre_csv = NOMBRES_API.get(nombre_normalizado, nombre_normalizado)

    for pais in paises or []:
        existente = normalizar_texto(pais["nombre"])
        if existente == nombre_normalizado:
            return True
        if NOMBRES_API.get(existente, existente) == nombre_csv:
            return True
    return False

#Consulta la API y devuelve un diccionario con el formato del csv, o None si falla
def consultar_api_pais(nombre):
    url = "https://countries.dev/name/" + quote(nombre_para_consulta(nombre))
    #La API rechaza peticiones sin User-Agent, por eso se indica explicitamente
    peticion = Request(url, headers={"User-Agent": "TPI-paises/1.0", "Accept": "application/json"})

    try:
        with urlopen(peticion, timeout=10) as respuesta:
            contenido = json.load(respuesta)
    except HTTPError as error:
        if error.code == 404:
            print("Pais no encontrado.")
        elif error.code in (401, 403):
            print("Error de autorizacion con la API. Revise las credenciales.")
        elif error.code == 429:
            print("Error. Demasiadas consultas a la API. Intente mas tarde.")
        else:
            print(f"Error en la respuesta de la API. Codigo: {error.code}")
        return None
    except TimeoutError:
        print("Error. La consulta a la API tardo demasiado. Intente otra vez.")
        return None
    except URLError:
        print("Error de conexion con la API. Revise su conexion e intente otra vez.")
        return None
    except (ValueError, UnicodeDecodeError):
        print("Error. La API devolvio una respuesta invalida.")
        return None

    #La API puede devolver una lista vacia cuando no hay coincidencias
    if not isinstance(contenido, list) or not contenido:
        print("Pais no encontrado.")
        return None

    datos = contenido[0]
    try:
        nombre_api = datos["name"]
        poblacion = datos["population"]
        superficie = datos["area"]
        continente = datos["region"]
    except (KeyError, TypeError):
        print("Error. La API devolvio datos incompletos.")
        return None

    #No se guarda nada si falta algun dato o si no son numeros
    try:
        poblacion = str(int(poblacion))
        superficie = str(int(superficie))
    except (TypeError, ValueError):
        print("Error. La API devolvio datos incompletos.")
        return None

    if not nombre_api or not continente:
        print("Error. La API devolvio datos incompletos.")
        return None

    return {
        "nombre": nombre_para_csv(nombre_api),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": CONTINENTES_API.get(normalizar_texto(continente), sin_tildes(continente))
    }

#Muestra los datos del pais consultado
def mostrar_pais_api(pais):
    print("Datos del pais consultado:")
    print(f"Nombre: {pais['nombre']}")
    print(f"Poblacion: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']}")
    print(f"Continente: {pais['continente']}")

#Pide una respuesta S/N y vuelve a preguntar si no es valida
def comprobar_si_no():
    while True:
        respuesta = input().strip().upper()
        if respuesta in ("S", "N"):
            return respuesta
        print("Error. Ingrese S o N.")

#Consulta un pais por API y lo guarda solo si el usuario lo confirma
def pais_api(paises):
    try:
        print("Ingrese el nombre del pais a consultar: ")
        nombre = input().strip()
        if not nombre:
            print("Error. Ingrese un nombre de pais.")
            return

        pais = consultar_api_pais(nombre)
        if pais is None:
            return

        mostrar_pais_api(pais)

        #Evita agregar dos veces el mismo pais, aunque venga con otro nombre
        if pais_existe(paises, pais["nombre"]):
            print("El pais ya existe en el archivo CSV. No se agrego ningun registro.")
            return

        print("¿Desea agregar este pais al archivo CSV? (S/N)")
        if comprobar_si_no() == "S":
            guardar_pais_nuevo(paises, pais)
        else:
            print("No se guardo ningun dato.")
    except Exception as error:
        print(f"Error inesperado al consultar la API: {error}")