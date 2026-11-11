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
    with open("paises.csv", "r", encoding="utf-8",  newline='') as archivo:
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
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writerow(nuevo_pais)

def modificar_pais(paises):
    columnas = ["nombre", "poblacion", "superficie", "continente"]

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


