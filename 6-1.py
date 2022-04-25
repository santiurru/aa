#Dada la siguiente lista [12, 23, 5, 29, 92, 64] realiza las siguientes operaciones y vete mostrando
#la lista resultante por pantalla:
#1. Elimina el último número y añádelo al principio.
#2. Mueve el segundo elemento a la última posición.
#3. Añade el número 14 al comienzo de la lista.
#4. Suma todos los números de la lista y añade el resultado al final de la lista.
#5. Fusiona la lista actual con la siguiente: [4, 11, 32]
#6. Elimina todos los números impares de la lista.
#7. Ordena los números de la lista de forma ascendente.
#8. Vacía la lista.

lista=[12, 23, 5, 29, 92, 64]
print(lista)

lista.pop()
lista.insert(0,64)
print(lista)        #1      [64, 12, 23, 5, 29, 92]

l=len(lista)        #=6
#print(l)           #muestra el largo de la lista

seg=lista[1]
#print(seg)
lista.pop(1)
lista.append(seg)
print(lista)        #2