#Crea un programa que reciba 5 números del usuario y muestre el mayor de todos por pantalla.

a=int(input("introduzca el valor 1:"))
b=int(input("introduzca el valor 2:"))
c=int(input("introduzca el valor 3:"))
d=int(input("introduzca el valor 4:"))
e=int(input("introduzca el valor 5:"))
lista=[a, b, c, d, e]
x=a
for i in lista:
  if i>=x:
    x=i
print("el mas alto es:", x)