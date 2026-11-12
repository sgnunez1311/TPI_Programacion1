import csv
#Usado para pedir un numero, comprobar que sea uno correcto y devolverlo
def comprobar_num():
    numero = input()
    while not numero.isdigit():
        print("Error, ingrese un numero entero.")
        numero = input("Intente de nuevo: ")
    numero = int(numero)
    return numero
#Usado para comprobar una palabra, comprobar que sea correcta y devolverla
def comprobar_palabra():
    palabra = input()
    while not palabra.isalpha:
        print("Error. Use solo letras.")
    return palabra
#Usado para escribir los datos del csv dentro del programa y guarardarlos para futuras modificaciones
def iniciar_csv():
    #creamos un diccionario vacio para guardar los paises en el csv
    paises = []

    #Abrimos el archivo para leer la informacion que ya contiene
    with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:
        #guardamos la informacion en una variable
        lector = csv.DictReader(archivo)
        #leemos diccionario por diccionario y lo guardamos en la variable "fila"
        for fila in lector:
        #Agregamos cada diccionario por separado a la lista "paises"
            paises.append(fila)

    return paises
#Usado para agregar un pais nuevo
def pais_nuevo():

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

    #definimos las columnas
    columnas = ["nombre", "poblacion", "superficie", "continente"]

    #Iniciamos el archivo en modo "a" para que se agregue la informacion y no borre todo
    with open("paises.csv", "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas, lineterminator="\n")
        escritor.writerow(nuevo_pais)
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
        with open ("paises.csv", "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(paises)
    else:
        print("Pais no encontrado.")
#Busca un pais y lo muestra
def buscar_pais():
    print("Ingrese un pais a buscar: ")
    buscar = comprobar_palabra()
    with open("paises.csv","r", encoding="utf-8", newline="") as archivo:

        lector = csv.DictReader(archivo)

        encontrado = False
        for pais in lector:
            if buscar.lower() in pais["nombre"].lower():
                print(pais)
                encontrado = True
        if encontrado == False:
            print("Pais no encontrado.")
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

        case 2:
            suma = 0
            promedio = 0
            cantidad = len(paises)

            with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:

                lector = csv.DictReader(archivo)

                for fila in lector:
                    suma += int(fila["poblacion"])
                promedio = suma / cantidad
                promedio = round(promedio, 2)
                print("El promedio de poblacion en todos los paises es de:",promedio)

        case 3:
            suma = 0
            promedio = 0
            cantidad = len(paises)

            with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:

                lector = csv.DictReader(archivo)

                for fila in lector:
                    suma += int(fila["superficie"])
                promedio = suma / cantidad
                promedio = round(promedio, 2)
                print("El promedio de superficie en todos los paises es de:",promedio)

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