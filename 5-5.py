#Mejora el programa anterior para que solo permita 3 intentos. Cada vez vez que el usuario introduzca
#datos de acceso incorrectos el programa mostrará el mensaje: “Datos incorrectos. Le quedan X
#intentos.”, siendo X el número de intentos restantes. Tras el tercer fallo el programa mostrará el
#mensaje “Has agotado todos tus intentos.” y finalizará

intentos=3
while intentos > 0:
  user=str(input("nombre de usuario:"))
  pwd=str(input("contraseña:"))
  if user=="root" and pwd=="toor":
    print("Bienvenido")
    break
  else:
    print("acceso fallido")
    intentos=intentos-1
    print("le quedan", intentos, "intentos")
if intentos==0:
  print("Has agotado todos tus intentos")