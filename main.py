#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

#Ingrese num: 1
#Ingrese num: 7
#La suma es 20

number1 = int(input("""In this exercise i nedd your enter two number and i show you the sum of the number that are between to two number that your insert
Please enter the number 1: """))
number2= int(input("Please enter the number 2: "))

if number1 > number2:
    number1, number2 = number2, number1 #Re-order the numbers first from small to bigger

sum=0   
i=number1+1

while i < number2:
    sum += i
    i +=1

print(f"""The sum is: {sum}""")