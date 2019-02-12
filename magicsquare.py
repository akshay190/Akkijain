def MagicSquare():
	ms=[]
	n=int(input("Enter a ODD--Number For Magic Square "))
	for i in range(n):
		l=[]
		for j in range(n):
			l.append(0)
		ms.append(l)
	i=n//2
	j=n-1
	num=n*n
	c=1
	while(c<=num):
		if(i==-1 and j==n):
			j=n-2
			i=0
		elif(j==n):
			j=0
		elif(i<0):
			i=n-1
		if(ms[i][j]!=0):
			j=j-2
			i=i+1
			continue
		else:
			ms[i][j]=c
			c=c+1
		i=i-1
		j=j+1
	for i in range(n):
		for j in range(n):
			print(ms[i][j],end=" ")
		print()


MagicSquare()		
