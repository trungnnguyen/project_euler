for a in range(1,1000):
	for b in range(1,a):
		csqr=(a**2)+(b**2)
		c=(pow(csqr,0.5))
		if(a+b+c==1000):
			print int(a*b*c)	
