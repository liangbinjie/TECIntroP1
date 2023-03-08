opciones = []
def menuMonomios():
    print("Has ingresado al modulo de monomios, que deseas realizar?")
    print("1) Suma de monomios\n"+
        "2) Resta de monomios\n"+
        "3) Multiplicacion de monomios\n"+
        "4) Division\n"+
        "5) Salir")
    opcion = int(input("> "))
    corriendo = 1
    while corriendo != 0:
       
        if opcion == 1:
            sumayresta()
            input("Enter para continuar...")
            break

        elif opcion == 2:
            sumayresta()
            input("Enter para continuar...")
            break
        
        elif opcion == 3:
            multiplicacion()
            input("Enter para continuar...")
            break

        elif opcion == 4:
            division()
            input("Enter para continuar...")
            break
        
        elif opcion == 5:
            corriendo = 0

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion = int(input("> "))


def sumayresta():
    m1 = int(input("Ingrese el primer archivo del monomio (1-13): "))
    m2 = int(input("Ingrese el segundo archivo del monomio (1-13): "))
    if 13 >= m1 > 0 and 13>=m2>0:
        a1 = open(f'Archivos/Mono{m1}.txt', "r") # archivo 1
        a2 = open(f'Archivos/Mono{m2}.txt', "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        if mono1[2] == mono2[2]:
            print(f'{mono1[0]+mono2[0]}{mono1[1]}{mono1[2]}')
            
        else: # si no son semejantes, m23 m9 1taco pg
            operador = '+'
            if mono2[0] < 0: # verificamos si el elemento del monomio es negativo
                operador = ''
            print(f'{mono1[0]}{mono1[1]}{mono1[2]}{operador}{mono2[0]}{mono2[1]}{mono2[2]}')

    else:
        print("No existe este archivo")


def multiplicacion():
    m1 = int(input("Ingrese el primer archivo del monomio (1-13): "))
    m2 = int(input("Ingrese el segundo archivo del monomio (1-13): "))
    if 13 >= m1 > 0 and 13>=m2>0:
        a1 = open(f'Archivos/Mono{m1}.txt', "r") # archivo 1
        a2 = open(f'Archivos/Mono{m2}.txt', "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(f'{mono1[0]*mono2[0]}{mono1[1]}{mono1[2]+mono2[2]}')
    
    else:
        print("Este archivo no existe")

def division():
    m1 = int(input("Ingrese el primer archivo del monomio (1-13): "))
    m2 = int(input("Ingrese el segundo archivo del monomio (1-13): "))
    if 13 >= m1 > 0 and 13>=m2>0:
        a1 = open(f'Archivos/Mono{m1}.txt', "r") # archivo 1
        a2 = open(f'Archivos/Mono{m2}.txt', "r") # archivo 2
        mono1 = a1.readline().split(";")
        mono2 = a2.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        mono2[0], mono2[2] = int(mono2[0]), int(mono2[2])
        print(f'{mono1[0]//mono2[0]}{mono1[1]}{mono1[2]-mono2[2]}')
    
    else:
        print("Este archivo no existe")

def potencia(): # potencia de un monomio
    m1 = int(input("Ingrese el primer archivo del monomio (1-13): "))
    potencia = int(input("Ingrese el valor de potencia: "))
    if 13 >= m1 > 0:
        a1 = open(f'Archivos/Mono{m1}.txt', "r") # archivo 1
        mono1 = a1.readline().split(";")
        mono1[0], mono1[2] = int(mono1[0]), int(mono1[2])
        print(f'{mono1[0]**potencia}{mono1[1]}{mono1[2]*potencia}')
    
    else:
        print("Este archivo no existe")