count = 1
c = 0
while count <= 9:
	b = 1
	while b <= count:
		print('%d*%d=%d'%(b,count,b*count),end="\t")
		b+=1
	print('')
	count+=1
