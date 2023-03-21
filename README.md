# TECIntroP1
Proyecto progra TEC Intro a la progra


---

## Manual de usuario

Para correr el proyecto, inicialmente se tiene que tener instalado Python, version 3.7+ preferiblemente.

Despues de descargar todos los archivos del proyecto. Abres el Python IDLE.

En el IDLE, abres el archivo `main.py`, con abrir ese archivo el proyecto correra sin problemas.

En el menu vas digitando las opciones que te da el programa. Si el la opcion no esta, te indicara que no esta esa opcion y tendras que ingresarlo nuevamente.

Es importante tener los documentos de los archivos de prueba metido en una carpeta llamada `Archivos`

Ya que si no estan metidos en esa carpeta, el programa no podra leer los archivos de los monomios y polinomios

---

### Monomios

Las funciones para hacer operaciones con los monomios estan divididos en cinco funciones diferentes, cada una con funcionalidades diferentes

Tambien tenemos una funcion que se encarga de ser como un menu, donde el usuario tendra que escoger cual funcion requiere realizar

Se describe a continuacion la funcionalidad de cada funcion

- **sumayresta():** se le pide al usuario que ingrese los nombres del archivo del monomio que requiere y este se encarga de hacer la operacion de suma y resta entre monomios. Durante el proceso, verificamos si los monomios son iguales, evaluando si su exponente en la posicion 2 de la lista es igual al otro monomio, si no son iguales, imprimos los monomios en forma de polinomio, en ese proceso tambien verificamos que el segundo monomio sea un numero negativo, si lo es, no le asignamos un operador, ya que si le asignamos, imprimiria `--`, lo cual resulta en que se convierta positivo, entonces establecemos que el operador sea un string vacio.

- **multiplicacionN():** esta funcion pide al usuario 2 archivos de los monomios. Durante el proceso, verificamos que al menos uno de los dos monomios sean un numero, osea, que tenga un exponente 0, en la posicion 2 del monomio, si no, se imprime un mensaje de error, donde se indica que no es posible multiplicarlo, ya que no es un numero lo que tenemos en el archivo.

- **multiplicacionM():**

- **division():**

- **potencia():**