archivo = open("names.txt", "r")
def listaNombres(f):
    names = sorted([n.strip('"') for n in f.read().split(',')])
    return names

def puntajePorNombre(a):
	i = 0
	res = 0
	while(i<len(a)):
		if(ord(a[i]) >= 64 and ord(a[i]) <= 90 ):
			res += ord(a[i])-64
		i+=1
	return res 
def puntajeTotal(a):
	i=0
	res=0
	while(i<len(a)):
		res += (i+1)*puntajePorNombre(a[i])
		i+=1
	return res


print puntajeTotal(listaNombres(archivo))
