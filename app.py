## funciones
def abrir_archivo():
    archivo = open("nombre.txt", "r")
    contenido = archivo.read()
    archivo.close()
    nombres = [n for n in contenido.split("\n") if n != ""]

    return nombres


def agregar_nombres(nombre_archivo, nombres):
    ## crear lista con nuevos nombres
    nuevos = []
    while True:
        try:
            cantidad = int(input("Elija cuantos nombres quiere agregar:\n"))
            break
        except ValueError:
            print("Eso no es un numero valido, intenta de nuevo")

    for c in range(cantidad):
        nuevo = input("Ingrese un nombre a agregar:\n")
        nuevos.append(nuevo)

    ## cambios en archivo
    archivo = open(nombre_archivo, "a")
    for c in nuevos:
        archivo.write(c + "\n")
    archivo.close()

    ## cambios en variable nombres
    for c in nuevos:
        nombres.append(c)

    return nombres


def borrar_nombre(nombre_archivo, nombres):
    if not nombres:
        print("No existe un nombre guardado aun\n")
        return []
    else:
        while True:
            try:
                borrar_varios_o_uno = int(
                    input(
                        "Quieres eliminar todos los nombres o solo uno en especifico?\n"
                        "1) Solo uno\n2) Todos\n"
                    )
                )
                break
            except ValueError:
                print(
                    "No es un numero valido, solo puede elegir 1 o 2, intente de nuevo"
                )

        if borrar_varios_o_uno == 1:
            buscar = input("Escriba el nombre a borrar:\n")

            if buscar in nombres:
                archivo = open(nombre_archivo, "w")
                nombres.remove(buscar)
                for c in nombres:
                    archivo.write(c + "\n")
                archivo.close()
                print("Se ha borrado el nombre")
                return nombres
            else:
                print(f"El nombre {buscar} no se encuentra en la lista de nombres")
                return nombres

        elif borrar_varios_o_uno == 2:
            seguro = input(
                f"Seguro que quieres borrar todos los nombres almacenados?, escribe SI para continuar\n"
                "De caso contrario escriba cualquier cosa para regresar al menu principal\n"
            )
            if seguro == "SI":
                archivo = open(nombre_archivo, "w")
                archivo.write("")
                archivo.close()
                print("Se ha borrado el nombre")
                return []
            else:
                return nombres

        else:
            print(
                "Esa no es una opcion valida, escriba 1 o 2 dependiendo que quieres hacer\n"
            )
            return nombres


def actualizar_nombre(nombre_archivo, nombres):
    if not nombres:
        print("No existe un nombre guardado aun\n")
        return nombres
    else:
        if len(nombres) == 1:
            nuevo = input("Ingrese el nuevo nombre:\n")

            ## cambios en memoria
            nombres[0] = nuevo

            ## cambios en archivo
            archivo = open(nombre_archivo, "w")
            archivo.write(nuevo + "\n")
            archivo.close()

            ## return
            return nombres

        else:
            
            buscar =  input("Ingrese el nombre a actualizar:\n")
            if buscar in nombres:
                nuevo = input("Ingrese el nuevo nombre:\n")

                ##cambios en memoria
                numero_indice = nombres.index(buscar)
                nombres[numero_indice] = nuevo

                ## cambios en archivo
                archivo = open(nombre_archivo, 'w')
                for c in nombres:
                    archivo.write(c + "\n")
                archivo.close()

                ##return
                return nombres

            else:
                print("Ese nombre no esta guardado\n")
                return nombres


def mostrar_nombre(nombres):
    if not nombres:
        print("No existe un nombre guardado aun\n")
    else:
        if len(nombres) == 1:
            print("El nombre guardado es:")
            print("\n".join(nombres))
        else:
            print("Los nombres guardados son:")
            print("\n".join(nombres))
    ## primera iteracion y menu repetitivo


def main():

    nombres = abrir_archivo()
    opcion = 1

    while opcion != 0:
        print(
            "---------Menu---------\n"
            "1) Ingresar nombres\n2) Borrar nombre\n3) Actualizar nombre\n4) Mostrar nombre\n5) Agregar nombres\n0) Salir"
        )
        try:
            opcion = int(
                input("Ingresa el numero corrrespondiente a lo que quieres hacer:\n")
            )
        except ValueError:
            print("Ingrese una opcion valida")
            continue

        ## opciones llamadas en main
        if opcion == 1:
            nombres = agregar_nombres("nombre.txt", nombres)

        elif opcion == 2:
            nombres = borrar_nombre("nombre.txt", nombres)

        elif opcion == 3:
            nombres = actualizar_nombre("nombre.txt", nombres)

        elif opcion == 4:
            mostrar_nombre(nombres)

        elif opcion == 0:
            print("Saliendo del programa...")

        else:
            print("Esa opcion no existe, intenta con otra")

    return


if __name__ == "__main__":
    main()
