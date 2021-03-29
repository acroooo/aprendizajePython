condicion = True
if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("No es un booleano")

numero = int(input("numero entre 1 - 3: "))

if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
else:
    numeroTexto = "numero tres"


print("numero ingresado : ", numeroTexto)