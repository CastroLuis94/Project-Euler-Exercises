def reverse(a):
	i = len(a)-1
	res = ""
	while(i>=0):
		res+=(a[i])
		i-=1
	return res

def Palindromo(a):
	return reverse(str(a)) == str(a)
	
a = 100
b = 100
res = 0
while(a<1000):
	while(b<1000):
		if(Palindromo(a*b)):
			if(res<a*b):
				res = a*b
		b+=1
	a+=1
	b=100
print res


