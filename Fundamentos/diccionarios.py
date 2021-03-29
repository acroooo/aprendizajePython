# compuesto de llaves, valor
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Managment System"
}

print(diccionario)

# largo
print(len(diccionario))
# accediendo
print(diccionario["IDE"])
# con get
print(diccionario.get("IDE"))
# modificando valores
diccionario["IDE"] = "Integrated development environment"

#accesos con for
#accedo a las llaves
for termino in diccionario:
    print(termino)
# ahora accedo a los valores
for termino in diccionario:
    print(diccionario[termino])

# otra opcion
for valor in diccionario.values():
    print(valor)

# nuevo elemento
diccionario["PK"] = "Primary Key"

#eliminar elemento
diccionario.pop("DBMS")

#limpiar
diccionario.clear()

#eliminar diccionario
del diccionario