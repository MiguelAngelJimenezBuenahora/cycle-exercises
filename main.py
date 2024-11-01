#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

#Ingrese un numero: 9
#9 x 1 = 9
#9 x 2 = 18
#9 x 3 = 27
#9 x 4 = 36
#9 x 5 = 45
#9 x 6 = 54
#9 x 7 = 63
#9 x 8 = 72
#9 x 9 = 81
#9 x 10 = 90

# Función para mostrar la tabla de multiplicar
def multiplyTable(number):
    i = 1
    print(f"Tabla de multiplicar del {number}:")
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i += 1

# Solicitar al usuario que ingrese un número
number = int(input(""""In this program ,your insert a number and i say you the multipler table from 1 to 10
    Please inser any number: """))
multiplyTable(number)


