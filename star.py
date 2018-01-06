row = 1
col = 1
i = 1
j = 1
while row <= 9 :
	print ("%d*%d=%d" % (i,j,i*j) ,end='')
	print("")
	j += 1
	row += 1
	while i <= j:
		print ("%d*%d=%d" (i,j,i*j) ,end='')
		print("")
		i += 1
	
