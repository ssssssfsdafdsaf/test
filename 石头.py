shitou = 1
jiandao = 2
bu  = 3


import random
while True:
	c = random.randint(1,3)
	i = int(input('请输入\n1.石头\n2.剪刀\n3.布\n'))

	if (i == 1 and c == 3) or (i == 2 and c == 1) or (i == 3 and c == 2):
		print('你输了')
	elif (i == 1 and c == 2) or (i == 2 and c == 3) or (i == 3 and c == 1):
		print('你赢了')
	else:
		print('平局')
	if i > 3:
		print('输入不合法')
