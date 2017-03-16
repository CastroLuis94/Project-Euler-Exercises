def SumaDeDigitos(a):
	res = 0
	i = 0
	while(i<len(a)):
		res += int(a[i])
		i += 1
	return res

a=2**1000
print SumaDeDigitos(str(a))
