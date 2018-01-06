acc = '1234'
pwd = '1234'
i = 1
a = 0

iacc = input('请输入账号:\n')
ipwd = input('请输入密码:\n')

if iacc != acc or ipwd != pwd:
	while i <= 3 and a == 0:
		i+=1
		iacc = input('请重新输入账号:\n')
		ipwd = input('请重新输入密码:\n')
		if iacc == acc and ipwd == pwd:
			a = 1
		if i == 3 and a == 0:
			print('系统繁忙，请稍后再试')
if iacc == acc and ipwd == pwd:
	print('登录成功')
	xuanze = input('请选择英雄范围\n1.adc\n2.坦克\n3.法师\n')
	if xuanze == '1':
			print('鲁班大师')
	if xuanze == '2':
			print('程咬金')
	if xuanze == '3':
			print('王昭君')

