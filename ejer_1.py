import numpy as np
print("¿Cuántos números quiere que contena su cadena?")
n=input()
n=int(n)
arreglo = []
print("Escriba los números:")
for i in range(n):
  k=input()
  k=int(k)
  arreglo.append(k)
print(arreglo)
print("¿Cuál es el número que quiere buscar?")
m=input()
m=int(m)
print("Las parejas de números son:")
for i in range (len(arreglo)):
  for j in range(i+1, len(arreglo)):
    if arreglo[i]+arreglo[j]==m:
      print("(" , arreglo[i] , "," , arreglo[j], ")") 
    else:
      print("Ninguna suma da el valor seleccionado")
