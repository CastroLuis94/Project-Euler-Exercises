def Primo(a):
	i = 2
	while(i*i<=a):
		if(a % i == 0): return False
		i+=1
	return True

i=2
res = 1
while(i<20):
	if(Primo(i)):
		aux = i
		while(aux < 20):
			aux = aux*i
		aux = aux/i
		res *= aux
	i += 1


print res
