nombres = ["Juan", "Karla", "Ricardo", "María"]
print(nombres)
#iterando lista
for elemento in nombres:
    print(elemento)

print("Largo de la lista: ", len(nombres))
print("Primer elemento: ", nombres[0])
print("Ultimo elemento: ", nombres[-1])

# parte 2
# imprimir el rango
print("Este es el rango 0-3", nombres[0:3], " se puede ver que no incluye el 3")
print("sin indicar el indice inicial", nombres[:3])
print("sin indicar el indice final", nombres[1:])
nombres[3] = "Hernán"
print(nombres[3], " => se cambio el elemento")

# compruebo que el elemento exista
if "Karla" in nombres:
    print("Existe el elemento")

# parte 3
# agregar un elemento
nombres.append("Lorenzo")

# insertar en el indice proporcionado
nombres.insert(1, "Octavio")

# remover elemento
nombres.remove("Octavio")

# remover el ultimo
nombres.pop()

# remover el indice indicado
del nombres[0]

# limpiar lista
nombres.clear()

# eliminar lista
del nombres

