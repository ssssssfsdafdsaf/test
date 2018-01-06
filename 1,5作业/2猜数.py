"""
import random
dian = random.randint(1,3)
"""
count = 1
import random
diannao = random.randint(1,100)
while count <= 10:
	wanjia = int(input('请输入数字\n'))
	if wanjia == diannao:
		print('恭喜你猜对了！')
		break
	elif wanjia > diannao:
		print('你猜大了')
	elif wanjia < diannao:
		print('你猜小了')
	count+=1
