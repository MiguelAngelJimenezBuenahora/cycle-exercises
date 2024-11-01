#Escriba un programa que entregue todos los divisores del número entero ingresado:

#Ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200

number = int(input("Please enter a number: "))

# Star a list for storage the dividers
dividers = []

# Bucle for found the dividers
for i in range(1, number + 1):
    if number % i == 0:
        dividers.append(i)

# print the results
print( dividers)
