## funciones
def ingresar_nombre(nombre):
    if nombre != "":
        print("Ya hay un nombre guardado")
        return nombre
    else:
        nombre = input("Ingrese un nombre:\n")
        return nombre


def borrar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
        return ""
    else:
        print("Se ha borrado el nombre")
        return ""


def actualizar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
        return ""
    else:
        nombre = input("Ingrese el nuevo nombre:\n")
        return nombre


def mostrar_nombre(nombre):
    if nombre == "":
        print("No existe un nombre guardado aun\n")
    else:
        print(f"El nombre guardado es: {nombre}")

    ##

    ## primera iteracion y menu repetitivo


nombre = ""
opcion = 1

while opcion != 0:
    print(
        "1) Ingresar nombre\n2) Borrar nombre\n3) Actualizar nombre\n4) Mostrar nombre\n0) Salir"
    )
    try:
        opcion = int(input("Ingresa lo que quieres hacer:\n"))
    except ValueError:
        print("Ingrese una opcion valida")
        continue

    ## opciones llamadas en main
    if opcion == 1:
        nombre = ingresar_nombre(nombre)

    elif opcion == 2:
        nombre = borrar_nombre(nombre)

    elif opcion == 3:
        nombre = actualizar_nombre(nombre)

    elif opcion == 4:
        mostrar_nombre(nombre)

    elif opcion == 0:
        print("Saliendo del programa...")

    else:
        print("Esa opcion no existe, intenta con otra")
