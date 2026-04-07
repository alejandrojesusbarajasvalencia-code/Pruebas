nombre = ""


def ingresar_nombre(nombre):
    nombre = input("Ingrese un nombre:\n")
    return nombre


def mostrar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre\n")
    else:
        print(f"El nombre guardado es: {nombre}")


def borrar_nombre(nombre):
    nombre = ""
    return nombre


def actualizar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
    else:
        nuevo = input("Ingrese el nuevo nombre:\n")
        nombre = nuevo
    return nombre


opcion = 1

while opcion != 0:
    print(
        "1) Ingresar nombre\n2) Borrar nombre\n3) Actualizar nombre\n4) Mostrar nombre\n0) Salir"
    )
    opcion = int(input("Ingresa lo que quieres hacer:\n"))

    if opcion == 1:
        nombre = ingresar_nombre(nombre)

    elif opcion == 2:
        nombre = borrar_nombre(nombre)
        if nombre == "":
            print("Se ha borrado el nombre")

    elif opcion == 3:
        nombre = actualizar_nombre(nombre)

    elif opcion == 4:
        mostrar_nombre(nombre)
