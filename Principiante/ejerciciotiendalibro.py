print("Proporcione los siguientes datos del libro")
nombre = input("Nombre del libro: ")
idLibro = int(input("ID del libro: "))
precio = float(input("Proporcione el precio: "))
envioGratuito = input("Indique si el envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    #Deberia ser una funcion para volver a llamarla
    envioGratuito = input("Indique si el envio es gratuito (True/False): ")

print(f"""
Nombre: {nombre}
id: {idLibro}
precio: {precio}
envio gratuito: {envioGratuito}
""")