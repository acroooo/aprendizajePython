#break
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    # rompe todo el ciclo
    print("Fin de ciclo")

# continue
for i in range(6):
    if i%2 != 0:
        continue
    else:
        print(i)