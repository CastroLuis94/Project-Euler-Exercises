def factorial(n):
	if(n==1):
		return 1;
	else:
		return n*factorial(n-1)

def SumaDeDigitos(a):
	a = str(a) 
	res = 0
	i = 0
	while(i<len(a)):
		res += int(a[i])
		i += 1
	return res

print SumaDeDigitos(factorial(100))
