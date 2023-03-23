def menuResultados():
    print("Has ingresado al modulo de resultados, que deseas realizar?")
    print("1) Ver cantidad de monomios semejantes utilizados\n"+
        "2) Ver cantidad de monomios no semejantes utilizados\n"+
        "3) Ver cantidad de polinomios ordenados utilizados\n"+
        "4) Ver cantidad de polinomios incompletos utilizados\n"+
        "5) Salir")
    opcion = int(input("> "))
    corriendo = 1
    while corriendo != 0:
       
        if opcion == 1:
            semejantes()
            input("Enter para continuar...")
            break

        elif opcion == 2:
            noSemejantes()
            input("Enter para continuar...")
            break
        
        elif opcion == 3:
            ordenados()
            input("Enter para continuar...")
            break

        elif opcion == 4:
            incompletos()
            input("Enter para continuar...")
            break
        
        elif opcion == 5:
            corriendo = 0

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion = int(input("> "))

def semejantes():
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    print(f'Se usaron {linea[0]} monomios semejantes')

def noSemejantes():
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    print(f'Se usaron {linea[1]} monomios no semejantes')

def ordenados():
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    print(f'Se usaron {linea[2]} polinomios ordenados')

def incompletos():
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    print(f'Se usaron {linea[3]} polinomios incompletos')