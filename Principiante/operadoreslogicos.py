# input devuelve string asi que hay que hacer conversion
a = int(input("Proporciona un valor: "))
valorMin = 0
valorMax = 5

# AND, los dos valores deben ser true
dentroRango = (a >= valorMin and a <= valorMax)

if(dentroRango):
    print("dentro del rango")
else:
    print("fuera de rango")

vacaciones = False
diaDescanso = False

# cualquiera de las dos opciones ( una u otra ) da true, se toma como verdadero todo.
if(vacaciones or diaDescanso):
    print("puedes ir al parque")
else:
    print("Tienes deberes que hacer")

#NOT invierte el resultado de la expresion booleana
print(not(vacaciones))