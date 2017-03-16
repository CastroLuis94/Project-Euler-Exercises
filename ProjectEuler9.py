a = 0
b = 0
res = 0
while(a<1000):
	while(b<1000):
		b+=1
		c = ((a**2)+(b**2))**(1.0/2)
		if(a+b+c==1000):
			res = a*b*c
			break
	a+= 1
	b = 0

print int(res)
