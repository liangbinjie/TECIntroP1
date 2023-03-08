from monomios import menuMonomios

opciones = [1,2,3,4,5]
cant_MS = 0 # cantidad de monomios semejnates utilzados
cant_MNS = 0 # cantidad de monomios no semenjantes utilizados
cant_PO = 0 # cantidad de polinomios ordenados utilziados
cant_PNO = 0 # cantidad de polinomios no ordenados utilizados


def menu():
    print("1) Monomios"+
      "\n2) Polinomios"+
      "\n3) Reportes"+
      "\n4) Salir")
    opcion = int(input("Ingrese una opcion: "))
    while opcion not in opciones:
        print("Opcion incorrecta, ingrese nuevamente")
        menu()
    if opcion == 1:
        menuMonomios()
        menu()
    elif opcion == 2:
        return
    elif opcion == 3:
        return
    elif opcion == 4:
        return
    elif opcion == 5:
        return


if __name__ == '__main__':
    menu()
