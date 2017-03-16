def Primo(a):
	i = 2
	while(i*i<=a):
		if(a % i == 0): return False
		i+=1
	return True

i = 3
res = 2
while(i<2000000):
	if(Primo(i)): res+= i
	i+=2

print res
