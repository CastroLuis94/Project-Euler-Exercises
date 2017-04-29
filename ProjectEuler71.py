import timeit

start = timeit.default_timer()
min_distancia = 1
min_numerador = 0
numerador = 1
d = 1
while d <= 1000000:
    if float(numerador/d) < float(3/7):
        if min_distancia > float(3/7) - float(numerador/d):
            min_distancia =  float(3/7) - float(numerador/d)
            min_numerador = numerador
        numerador +=1
    else:
        d += 1
   
    
 
    

print(min_numerador)
print(timeit.default_timer() - start)