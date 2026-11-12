import funciones

paises = funciones.iniciar_csv()

while True:
   print("Menu:")
   print("1. Agregar un pais nuevo.")
   print("2. Actualizar datos de un pais.")
   print("3. Buscar un pais por nombre")
   print("4. Filtrar paises")
   print("5. Ordenar paises")
   print("6. Mostrar estadisticas")
   print("7. Salir")

   print("¿Que desea hacer? ")
   opcion = funciones.comprobar_num()

   match opcion:
      case 1:
         funciones.pais_nuevo()
      case 2:
         funciones.modificar_pais(paises)
      case 3:
         funciones.buscar_pais()
      case 4:
         funciones.filtrar_paises(paises)
      case 5:
         funciones.ordenar_paises(paises)
      case 6:
         funciones.estadisticas(paises)
      case 7:
         print("Saliendo...")
         break
