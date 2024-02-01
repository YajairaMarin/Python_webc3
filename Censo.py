import random
censo=[]
alfabeto="aknajgucsehcgcasmcfhg"
numero=0
print("Creando censo...")

for i in range (500_000):
    aumento=random.randint(1,2)
    numero += numero

    letras= random.sample(alfabeto,5)
    nombre="".join(letras)
    edad=random.randint(18,99)
    impuestos=random.choice((True,True,True,Flase))
    censo.append([numero,nombre,edad,impuestos])
    if len(censo)%100_000==0:
        print("creados", len(censo), "registros")
print("censo creado...")
print("último registro",censo[-1])       

def busqueda_numero(lista, elemento):
    '''Busca registros por numero binaria'''
    inicio =0
    final=len(lista)-1
    while inicio <= final:
        medio=(inicio+finak)//2
        if lista [medio][0]==elemento:
            return lista[medio]
        elif lista [medio][0]<elemento:
            inicio= medio+1