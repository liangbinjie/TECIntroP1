from monomios import menuMonomios
from polinomio import menuPolinomios
from resultados import menuResultados
import os
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

opciones = [1,2,3,4,5]
resultados = open(path+"\\resultados.txt", "w")
resultados.write("0;0;0;0")
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
        menuPolinomios()
        menu()
    elif opcion == 3:
        menuResultados()
        menu()
    elif opcion == 4:
        exit()


if __name__ == '__main__':
    menu()
