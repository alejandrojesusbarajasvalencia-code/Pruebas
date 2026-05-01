## funciones
def abrir_archivo():
    archivo = open("nombre.txt", "r")
    contenido = archivo.read()
    archivo.close()
    return contenido


def ingresar_nombre(nombre_archivo, nombre):
    if nombre != "":
        print("Ya hay un nombre guardado, intente borrar el nombre o actualizarlo")
        return nombre
    else:
        nombre = input("Ingrese el nombre:\n")
        archivo = open(nombre_archivo, "w")
        archivo.write(nombre)
        archivo.close()
        return nombre


def borrar_nombre(nombre_archivo, nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
        return ""
    else:
        seguro=input(f"Seguro que quieres borrar el nombre: {nombre}?, escribe SI para continuar\n"
                     "De caso contrario escriba cualquier cosa para regresar al menu principal\n")
        if seguro == "SI":
            archivo = open(nombre_archivo, "w")
            archivo.write("")
            archivo.close()
            print("Se ha borrado el nombre")
            return ""
        else:
            return nombre


def actualizar_nombre(nombre_archivo, nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
        return ""
    else:
        nombre = input("Ingrese el nuevo nombre:\n")
        archivo = open(nombre_archivo, "w")
        archivo.write(nombre)
        archivo.close()
        print("Se ha guardado el nuevo nombre\n")
        return nombre


def mostrar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
    else:
        print(f"El nombre guardado es: {nombre}")

    ## primera iteracion y menu repetitivo


def main():

    nombre = abrir_archivo()

    opcion = 1

    while opcion != 0:
        print(
            "---------Menu---------\n"
            "1) Ingresar nombre\n2) Borrar nombre\n3) Actualizar nombre\n4) Mostrar nombre\n0) Salir"
        )
        try:
            opcion = int(input("Ingresa el numero corrrespondiente a lo que quieres hacer:\n"))
        except ValueError:
            print("Ingrese una opcion valida")
            continue

        ## opciones llamadas en main
        if opcion == 1:
            nombre = ingresar_nombre("nombre.txt", nombre)

        elif opcion == 2:
            nombre = borrar_nombre("nombre.txt", nombre)

        elif opcion == 3:
            nombre = actualizar_nombre("nombre.txt", nombre)

        elif opcion == 4:
            mostrar_nombre(nombre)

        elif opcion == 0:
            print("Saliendo del programa...")

        else:
            print("Esa opcion no existe, intenta con otra")

    return


if __name__ == "__main__":
    main()
