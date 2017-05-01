import timeit
import random
from itertools import permutations

def levanta_archivo(nombre):
    archivo = open(nombre, "r") 
    contenido = archivo.read()
    contenido = contenido.split('\n')
    res = []
    for string in contenido:
        res.append(string.split())
    for row in res:
        i = 0
        while i < len(row):
            row[i] = int(row[i])
            i+=1
    return res

matriz = levanta_archivo('ProjectEuler345.txt')

def suma_matriz(matriz,indices_usados,profundidad):
    indices_disponibles = set(range(len(matriz))) - indices_usados 
    if len(matriz) - profundidad - 1== 0:
        return matriz[profundidad][indices_disponibles.pop()]
    else:
        maximo = 0
        k = 0
        posible_res = 0
        for k in indices_disponibles:
            res = matriz[profundidad][k]
            copia = set(indices_usados)
            copia.add(k)
            res += suma_matriz(matriz,copia,profundidad+1)
            if posible_res < res:
                posible_res = res
        return posible_res
        
start = timeit.default_timer()
print(suma_matriz(matriz,set(),0))
print(timeit.default_timer() - start)

         
        


                       


    
            
            
           
