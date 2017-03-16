def SumaGaus(n):
	return (n*(n+1)/2)

i=1
res=0
while(i<=100):
	res += i**2
	i+=1
res = (SumaGaus(100)**2) - res 
print res
