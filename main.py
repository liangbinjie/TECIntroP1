from monomios import menuMonomios
import os
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

opciones = [1,2,3,4,5]
resultados = open(path+"\\resultados.txt", "w")
resultados.write("0")
resultados.close()

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
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass


if __name__ == '__main__':
    menu()
