def es_tringular(numero):
    n = 2
    res = False
    suma_gauss = 1
    while suma_gauss < numero:
        suma_gauss += n
        n += 1
    return suma_gauss == numero


def valor_string(palabra):
    res = 0
    for letra in palabra:
        if(letra != '"'):
            res += ord(letra) -64
    return res

def levanta_archivo(nombre):
    archivo = open(nombre, "r") 
    contenido = archivo.read()
    contenido = contenido.split(',')
    return contenido

lista_palabras = levanta_archivo('project42.txt')
total = 0
for palabra in lista_palabras:
    if es_tringular(valor_string(palabra)):
        total += 1
print(total)