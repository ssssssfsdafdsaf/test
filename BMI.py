shengao = float(input("请输入你的身高"))
tizhong = float(input("请输入你的体重"))
BMI = float(tizhong/(shengao**2))

print("你的BMI指数为:%d"%BMI)

if BMI < 18.5:
	print("过轻")
elif BMI >= 18.5 and BMI < 25:
	print("正常")
elif BMI >= 25 and BMI < 28:
	print("过重")
elif BMI >= 28 and BMI < 32:
	print("肥胖")
elif BMI > 32:
	print("严重肥胖")
