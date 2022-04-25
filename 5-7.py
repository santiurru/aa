#Mejora el programa anterior, de forma que el usuario pueda introducir tantos números como quiera.
#El programa solicitará números al usuario hasta que introduzca la palabra “fin”. Entonces mostrará
#el mayor de todos por pantalla.

a = input("ingrese un valor:")
if a=="fin":
  print("no ingresó ningun valor")
else:
  a=int(a)
  max=a
  while a!="fin":
    if a>=max:
      max=a
    a=input("ingrese otro valor:")
    if a!="fin":
      a=int(a)
  print("el valor mas alto es:", max)