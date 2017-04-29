def crear_lista(tamanio):
    res = list()
    for elem in range(tamanio+1):
        res.append(0)
    return res

def es_un_cuadrado(numero):
    i = 1
    while (i*i < numero):
        i+=1
    return (i*i) == numero

res = crear_lista(1000)
a = 1
b = 1
while a <= 1000 :
    b = a + 1
    while a+b <= 1000:
        c = (a**2)+(b**2)
        if es_un_cuadrado(c):
            c = int(c**(1/2.))
            if a+b+c <= 1000:
                res[a+b+c] += 1
        b += 1
    a += 1
 
m = max(res)
i = 0
while (i < len(res)):
    if res[i] == m:
        print(i)
        break
    i += 1