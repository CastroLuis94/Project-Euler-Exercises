class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def suma(punto1,punto2):
    return Punto(punto1.x+punto2.x,punto1.y+punto2.y)

class Triangulo:
    def __init__(self,punto1,punto2,punto3):
        self.A1 = punto1
        self.A2 = punto2
        self.A3 = punto3
    
    def orientacion(self):
        return (((self.A1).x - (self.A3).x) * ((self.A2).y - (self.A3).y) - ((self.A1).y - (self.A3).y) * ((self.A2).x - (self.A3).x))

    def esta_contenido(self,punto):
        t1 = (Triangulo(self.A1,self.A2,punto)).orientacion()
        t2 = (Triangulo(self.A2,self.A3,punto)).orientacion()
        t3 = (Triangulo(self.A3,self.A1,punto)).orientacion()
        t4 = self.orientacion()
        if t1 > 0 and t2 > 0 and t3 > 0 and t4 > 0:
            return True
        else:
            if t1 < 0 and t2 < 0 and t3 < 0 and t4 < 0:
                return True
            else:
                return False


def levanta_archivo(nombre):
    archivo = open(nombre, "r") 
    contenido = archivo.read()
    contenido = contenido.split('\n')
    def string_a_int(lista_string):
        res = []
        for num in lista_string:
            elem = num.split(',')
            for n in elem:
                res += [int(n)]
        return res
    return string_a_int(contenido)

def triangulos(entrada):
    i = 0
    res = []
    while i+5 < len(entrada):
        p1 = Punto(entrada[i],entrada[i+1])
        p2 = Punto(entrada[i+2],entrada[i+3])
        p3 = Punto(entrada[i+4],entrada[i+5])
        i += 6
        res.append(Triangulo(p1,p2,p3))
    return res
entrada = levanta_archivo('project102.txt')
lista_triangulos = triangulos(entrada)
res = 0  
for t in lista_triangulos:
    if t.esta_contenido(Punto(0,0)):
        res += 1
print(res)

