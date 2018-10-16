# Autor: Luis Humberto Burgueño Paz
# Muestra al usuario un menú con el que puede decidir si quiere dividir, encontrar el número mayor, o salir del programa


# Muestra un menú al usuario y lee la opción que el usuario introduce.
def leerOpcionMenu():
   print("Misión 07. Ciclos while")
   print("Autor: Luis Humberto Burgueño Paz")
   print("Matrícula: A01376470")
   print("1. Calcular Divisiones")
   print("2. Encontrar el mayor")
   print("3. Salir")
   opcion = int(input("Teclea tu opción: "))
   return opcion


# Realiza una división utilizando ciclos con restas e imprime el resultado
def dividir(dividendo, divisor):
   cociente = 0
   dividendoInicial=dividendo
   while dividendo>=divisor:
       dividendo = dividendo-divisor
       cociente = cociente+1
   print("%d / %d = %d, sobra %d" % (dividendoInicial, divisor, cociente, dividendo))


# Encuentra el mayor de una serie de números que el usuario introduce
def encontrarMayor():
    numero = 0
    print("Teclea una serie de números para encontrar el mayor")
    numeroUsuario = 0
    while numeroUsuario != -1:
        numeroUsuario = int(input("Teclea un número [-1 para salir]: "))
        if numeroUsuario > numero:
            numero = numeroUsuario
    if numero == 0:
        print("No hay valor mayor")
    else:
        print("El mayor es", numero)


#Función Principal. Llama a las otras funciones
def main():
   opcion = leerOpcionMenu()
   while opcion != 3:
       if opcion == 1:
           print("Calculando divisiones")
           dividendo = int(input("Dividendo: "))
           divisor = int(input("Divisor: "))
           dividir(dividendo, divisor)
       elif opcion == 2:
           encontrarMayor()


       elif opcion < 1 or opcion > 3:
           print("ERROR, teclea 1, 2 o 3")
       opcion = leerOpcionMenu()
   print("Gracias por usar este programa, regresa pronto.")


main()
