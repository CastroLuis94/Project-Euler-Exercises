archivo = open("numeros.txt", "r")
contenido = archivo.read()

def lista(a):
	i = 0
	res=[]
	while(i+1< len(a)):
		res.append(int(a[i]+a[i+1]))
		i+=3
	return res
def Matriz(a):
	v = lista(a)
	i = 0
	cantidadDeElementos = 2**i
	vectorAux = []
	res = []
	while(i<len(v)):
		vectorAux.append(v[i])
		if(len(vectorAux)==cantidadDeElementos):
			res.append(vectorAux)
			vectorAux = []
			cantidadDeElementos += 1
		i+=1
	return res
def SumaPosiblesCaminos(a):
	a= Matriz(a)
	i=1
	caminos = [(a[0],0)]
	caminosAux = []
	while(i<len(a)):
		k=0 
		while(k < len(caminos)):
			numero = a[i][caminos[k][1]] 
			tupla = (caminos[k][0]+[(numero)],caminos[k][1])
			caminosAux.append(tupla) 
			numero = a[i][caminos[k][1]+1] 
			tupla = (caminos[k][0]+[(numero)],caminos[k][1]+1)
			caminosAux.append(tupla) 
			k+=1
		caminos = caminosAux
		caminosAux = []
		i+=1
	j = 0 
	maximo = 0
	while(j < len(caminos)):
		if(maximo< sum(caminos[j][0])):
			maximo = sum(caminos[j][0])
		j += 1
	return maximo
print SumaPosiblesCaminos(contenido)


