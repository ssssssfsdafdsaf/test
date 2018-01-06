acc = '123456'
pwd = '123456'

iacc = input("请输入用户名：\n")
ipwd = input('请输入密码\n')

if iacc == acc and ipwd == pwd:
	print('登陆成功！')
else:
	print('登陆失败！')
