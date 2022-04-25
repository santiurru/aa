#Escribe un programa que solicite al usuario un nombre de usuario y contraseña. El programa
#mostrará el mensaje “¡Bienvenido!” si el usuario introduce los siguientes datos:

user=str(input("nombre de usuario:"))
pwd=str(input("contraseña:"))
if user=="root" and pwd=="toor":
  print("Bienvenido")
else:
  print("acceso fallido")