import os
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

def menuMonomios():
    print("Has ingresado al modulo de monomios, que deseas realizar?")
    print("1) Suma y resta de monomios\n"+
        "2) Multiplicacion de monomios\n"+
        "3) Division\n"+
        "4) Potencia de un monomio\n"+
        "5) Salir")
    opcion = int(input("> "))
    corriendo = 1
    while corriendo != 0:
       
        if opcion == 1:
            sumres = input("Que desea hacer\n1) Restar\n2) Sumar\n> ")
            if sumres == "1":
                resta()
            elif sumres == "2":
                suma()
            input("Enter para continuar...")
            break

        elif opcion == 2:
            opcionM = int(input("Desea multiplicar numero por monomio o monomio por monomio\n1) Numero por monomio\n2) Monomio por monomio\n> "))
            if opcionM == 1:
                multiplicacionN()
            elif opcionM == 2:
                multiplicacionM()
            else:
                print("Opcion invalida")
            input("Enter para continuar...")
            break
        
        elif opcion == 3:
            division()
            input("Enter para continuar...")
            break

        elif opcion == 4:
            potencia()
            input("Enter para continuar...")
            break
        
        elif opcion == 5:
            corriendo = 0

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion = int(input("> "))


def suma():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        m2 = input("Ingrese el nombre del segundo archivo del monomio: ")
        print(path+"\Archivos"+f"\{m1}.txt")
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        a2 = open(path+"\Archivos"+f"\{m2}.txt", "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(mono1, "+", mono2)
        if mono1[2] == mono2[2]:
            print(f'{mono1[0]+mono2[0]}{mono1[1]}{mono1[2]}')
            
        else: # si no son semejantes 
            operador = '+'
            if mono2[0] < 0: # verificamos si el elemento del monomio es negativo
                operador = '' # si lo es, no le asignamos un operador
            print(f'{mono1[0]}{mono1[1]}{mono1[2]}{operador}{mono2[0]}{mono2[1]}{mono2[2]}')

    except FileNotFoundError:
        print("Archivo no existe")


def resta():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        m2 = input("Ingrese el nombre del segundo archivo del monomio: ")
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        a2 = open(path+"\Archivos"+f"\{m2}.txt", "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(mono1, "-", mono2)
        if mono1[2] == mono2[2]:
            print(f'{mono1[0]-mono2[0]}{mono1[1]}{mono1[2]}')
            
        else: # si no son semejantes 
            operador = '-'
            if mono2[0] < 0: # verificamos si el elemento del monomio es negativo
                operador = '+' # si lo es, no le asignamos un operador
                mono2[0]*=-1
            print(f'{mono1[0]}{mono1[1]}{mono1[2]}{operador}{mono2[0]}{mono2[1]}{mono2[2]}')

    except FileNotFoundError:
        print("Archivo no existe")

# resta()
        
def multiplicacionN():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        m2 = input("Ingrese el nombre del segundo archivo del monomio: ")
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        a2 = open(path+"\Archivos"+f"\{m2}.txt", "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(mono1, "*", mono2)
        if mono1[2] == 0 or mono2[2] == 0:
            print(f'{mono1[0]*mono2[0]}{mono1[1]}{mono1[2]+mono2[2]}')
        else:
            print("No existe un numero, escoja un archivo que contenga un monomio, es decir, la potencia elevado a la 0")

    except FileNotFoundError:
        print("Archivo no existe")

def multiplicacionM():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        m2 = input("Ingrese el nombre del segundo archivo del monomio: ")
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        a2 = open(path+"\Archivos"+f"\{m2}.txt", "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(mono1, "*", mono2)
        print(f'{mono1[0]*mono2[0]}{mono1[1]}{mono1[2]+mono2[2]}')

    except FileNotFoundError:
        print("Archivo no existe")

def division():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        m2 = input("Ingrese el nombre del segundo archivo del monomio: ")
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        a2 = open(path+"\Archivos"+f"\{m2}.txt", "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(mono1, "/", mono2)
        print(f'{mono1[0]//mono2[0]}{mono1[1]}{mono1[2]-mono2[2]}')

    except FileNotFoundError:
        print("Archivo no existe")

def potencia():
    try:
        m1 = input("Ingrese el nombre del primer archivo del monomio: ")
        potencia = int(input("Ingrese el valor de potencia: "))
        a1 = open(path+"\Archivos"+f"\{m1}.txt", "r") # archivo 1
        mono1 = a1.readline().split(";")
       
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        print(mono1, "**", potencia)
        print(f'{mono1[0]**potencia}{mono1[1]}{mono1[2]*potencia}')

    except FileNotFoundError:
        print("Archivo no existe")