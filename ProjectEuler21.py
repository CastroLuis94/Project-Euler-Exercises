def SumaDivisores(a):
	i=2
	res=1
	while(i<=a/2):
		if(a % i ==0):
			res+=i
		i+=1
	return res
def amigable(a):
	b = SumaDivisores(a)
	return a == SumaDivisores(b) and a != b 

i = 2
res = 0
while(i<10000):
	if(amigable(i)):
		res += i
	i+=1
print res
