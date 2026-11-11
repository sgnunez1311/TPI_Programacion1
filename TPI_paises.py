import funciones

paises = funciones.iniciar_csv

print("Menu:")
print("1. Agregar un pais nuevo.")
print("2. Actualizar datos de un pais.")
print("3. Buscar un pais por nombre")
print("4. Filtrar paises")
print("5. Ordenar paises")
print("6. Mostrar estadisticas")

print("¿Que desea hacer? ")
opcion = funciones.comprobar_num()

match opcion:
   case 1:
      funciones.pais_nuevo
   case 2:
      print("")
   case 3:
      print("")
   case 4:
      print("")
   case 5:
      print("")
   case 6:
      print("")
