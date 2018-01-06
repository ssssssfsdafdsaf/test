zh = 123456
mm = "abc"



number = int(input("请输入账号\n"))
passwd = input("请输入密码\n")


if number == zh and passwd == mm:
	print("登陆成功！") 
elif number != zh and passwd == mm:
	print("账号错误！")
elif number == zh and passwd != mm:
	print("密码错误！")
else:
	print("账号、密码错误！")
