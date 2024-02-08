ingreso = input("") #Escribe por pantalla los datos 
cadena = ingreso.split(' ') #Identifica el espacio para el segundo número

if len(cadena) == 2: #Resticción para que sólo se digite un espacio
    secuencia = cadena[0]
    buscar = cadena[1]

    try:
        numeros = [int(x) if x != '' else 0 for x in secuencia.split(',')] #convierte en lista numérica reconociendo la coma
    except ValueError:
        print("No digita correctamnte los números")
        exit()

    try:
        numero = int(buscar)
    except ValueError:
        print("No digita correctamente el número")
        exit()

    parejas = []
    #Ciclo para identificar los números cuya suma de el seleccionado
    for i, num1 in enumerate(numeros):
        for num2 in numeros[i + 1:]:
            if num1 + num2 == numero:
                parejas.append((num1, num2))

    print(f"Parejas cuya suma es {numero}: {parejas}")

else:
    print("digite correctamente la secuencia")