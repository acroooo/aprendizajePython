# Tuplas : mantienen el orden pero no se pueden modificar
frutas = ("naranja", "platano", "kiwi", "sandia")
print(frutas)

# largo de la tupla
print(len(frutas))

# accediendo al elemento
print(frutas[0])

# conversion para agregar elementos
frutasLista = list(frutas)
frutasLista[0] = "El modificado"
frutas = tuple(frutasLista)
print(frutas)

for fruta in frutas:
    print(fruta, end=" ")