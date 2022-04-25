#Escribe un programa que solicite dos números enteros al usuario y muestre por pantalla la suma de
#todos los números enteros que hay entre los dos números (ambos números incluidos).
ini=int(input("ingrese el numero de inicio:"))
fin=int(input("ingrese el numero del final:"))
suma=0
for i in range (ini, fin+1):
    suma=suma+i
print("el total de la suma es:", suma)
