account =  '123456'
passwd = 'abc'
money = 500

myaccount = input('请输入账号\n')
mypasswd = input('请输入密码\n')

if myaccount == account and mypasswd == passwd:
	mode = int(input('请输入您要执行的操作\n1.取款\n2.存款\n'))
	if mode == 1:
		mymoney = int(input('请输入取款金额\n'))
		if mymoney <= 500:
				print('取款成功!\n账户余额%d'%(money-mymoney))
		elif mymoney > 500:
				print('余额不足！')
	if mode == 2:
		imoney = int(input('请输入存款金额'))
		print('存款成功\n您的余额为%d'%(imoney+money))
	
else:
	print('账号或密码不正确')
