count = 0
jishu = 0
oushu = 0
while count < 101:
	if count%2 == 0:
		oushu+=count
	if count%2 != 0:
		jishu+=count
	count+=1
	zonghe = (oushu+jishu)
print('偶数和是%d'%oushu)
print('奇数和是%d'%jishu)
print('总和是%d'%zonghe)
		 
