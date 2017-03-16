def Primo(a):
	i = 2
	while(i*i<=a):
		if(a % i == 0): return False
		i+=1
	return True

res = 0
i = 0
iterador = 2
while(i<10001):
	if(Primo(iterador)):
		i+=1
		res = iterador
	iterador+=1
print res
