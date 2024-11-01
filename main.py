#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

#Ingrese num: 10
#1 2 4 8 16 32 64 128 256 512 1024

import math
number = int(input(""""In this exercise your inset a number and i show you the multiply of  from 0 to the number do your insert
Please insert the number:"""))
i =0
while i <= number:
    result = math.pow(2,i)
    print(result)
    i+= 1
