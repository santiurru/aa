#Mejora el programa anterior para que muestre por separado la suma de los números pares y los impares

ini=int(input("ingrese el numero de inicio:"))
fin=int(input("ingrese el numero del final:"))
suma_par=0
suma_impar=0
for i in range (ini, fin+1):
    if i%2==0:
        suma_par=suma_par+i
    else:
        suma_impar=suma_impar+i
print("los pares suman", suma_par, "y los impares suman", suma_impar) 

