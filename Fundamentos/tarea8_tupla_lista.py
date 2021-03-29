"""
Dada la siguiente tupla, crear una lista que sólo
incluya los números menor que 5 utilizando un ciclo for:
tupla = (13, 1, 8, 3, 2, 5, 8)
"""

tupla = (13,1,8,3,2,5,8)

lista = list(tupla)
print(lista)

for i in lista:
    if(i > 5):
        lista.remove(i)

print(lista)

# otra solucion
# utilizar append para agregar solo los numeros indicados
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)