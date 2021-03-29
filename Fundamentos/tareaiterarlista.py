# Iterar una lista de 1 - 10 e imprimir números divisibles entre 3
lista = [0,1,2,3,4,5,6,7,8,9,10]

for numero in lista:
    if(numero%3 == 0):
        print(numero)
    else:
        continue

print("Fin del ciclo")


# Otra solucion
for i in range(10):
    if i % 3 == 0:
        print(i)