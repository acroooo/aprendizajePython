# set es una coleccion sin orden ni indices, tampoco tienen elementos
# repetidos y los elementos no se pueden modificar pero
# si agregar nuevos o eliminar existentes

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
planetas.add("Tierra")
print(planetas)
planetas.remove("Tierra")
print(planetas)
planetas.discard("Jupiter")
print(planetas)