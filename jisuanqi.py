x = int(input("请输入一个数字\n"))
o = input("请输入+-*/\n")
y = int(input("请输再输入一个数字\n"))

if o == "+":
	sum=x+y
elif o == "-":
	sum=x-y
elif o == "*":
	sum=x*y
elif o == "/":
	sum=x/y
else:
	print("叽叽")

print("结果是%s\n"%sum)
