# total= 10000
# password = input("请输入密码：")
# print(f"密码正确：{password}")
# number = int(input("请输入取款金额："))
# print(f"剩余金额为：{total-number}")



# print("# # # # # # # # # #")
# print("#  白 日 依 山 尽 #")
# print("#  黄 河 入 海 流 #")
# print("#  欲 穷 千 里 目 #")
# print("#  更 上 一 层 楼 #")
# print("# # # # # # # # # #")

# number1 = float(input("请输入第1个数："))
# number2 = float(input("请输入第2个数："))
# print(f"总和为：{number1-number2}")

# x = float(input("请输入第一个数："))
# y = float(input("请输入第二个数："))
# print(f"{x}-{y}={x-y}")
# print(f"{x}+{y}={x+y}")

# upper = float(input("请输入上底："))
# lower = float(input("请输入下底："))
# height = float(input("请输入高："))
# area = (upper+lower)*height/2
# print(f"梯形的面积：{area}")

# user = input("请输入账号：")
# password = input("请输入密码：")
# if user ==1888888888 and password == 666888:
#    print("完成登录")
# else:
#     print("登录失败")


# year = int(input("请输入年份："))
# if (year%10!=0 and year%4==0) or (year%400==0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


# number = int(input("请输入数字："))
# if number%2==0:
#     print("是偶数")
# elif number%2 != 0:
#     print("是奇数")
# else:
#     print("是0")


# money = float(input("请输入花费的金额："))
# if money >500:
#     print(f"应支付：{money * 0.8}")
# elif money >=300 and money<=500:
#     print(f"应支付:{money * 0.9}")
# elif money >=100 and money<300:
#     print(f"应支付:{money * 0.95}")
# elif money <100:
#     print(f"应支付:{money}")

#判断三角形
# a = int(input("请输入第一个边："))
# b = int(input("请输入第二个边："))
# c = int(input("请输入第三个边："))
# if a+b>c and b+c>a and c+a>b:
#     if a==b==c:
#         print("是等边三角形")
#     elif a==b or b==c or c==a:
#         print("是等腰三角形")
#     elif a!=b!=c:
#         print("是一般三角形")
# else:
#     print("不是三角形")

# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数： "))
# oper = input("请输入运算符号：")
# match oper:
#     case"+":
#         print(f"{num1}+{num2}={num1 + num2}")
#     case"-":
#         print(f"{num1}-{num2}={num1 -num2}")
#     case"*":
#         print(f"{num1}*{num2}={num1 * num2}")
#     case"/":
#         print(f"{num1}/{num2}={num1 / num2}")
#     case"_":
#         print("操作暂不支持！")

# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(f"和为：{sum}")

# sum=0
# for i in range(100,501):
#     if i%3==0:
#         sum+=i
# print(f"和为：{sum}")


# do = input("请输入你的动作：")
# match do :
#     case "w" | "W":
#         print("角色向上移动")
#     case "s" | "S":
#         print("角色向下移动")
#     case "a" | "A":
#         print("角色向左移动")
#     case "d" | "D":
#         print("角色向右移动")
#     case "跳" | "":
#         print("角色跳跃")
#     case "j" | "J":
#         print("角色发动攻击")
#     case "esc" | "ESC":
#         print("角色退出游戏")


# # 九九乘法表
# for i in range(1,10):      #控制第一个数
#      for j in range(1,i+1):   #控制第二个数
#          print(f"{j} x {i} ={j*i}", end="\t")
#      print()


# n = int(input("请输入直角三角形的边是多少："))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j,end="  ")
#     print()

# n = int(input("请输入金字塔高度："))
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()


# 国际象棋
# for i in range(8):
#     for j in range(8):
#         if (i+j)%2 ==0:
#             print("黑",end=" ")
#         else:
#             print("白",end=" ")
#     print()


# while True:
#     username=input("请输入用户名：")
#     password=input("请输入用户密码：")
#     if username =="" or password =="":
#         print("用户和密码不能为空！")
#         continue
#     elif username == "admin" and password == "666888":
#         print("登录成功，进入b站首页")
#         break
#     else:
#         print ("用户和密码错误，请重新输入！")


# i=1
# while i<=5:
#     username = input("请输入用户名：")
#     password = input("请输入用户密码：")
#     if username =="" or password =="":
#         print("用户和密码不能为空！")
#         i+=1
#         continue
#     elif username == "admin" and password == "666888":
#         print("登录成功，进入b站首页")
#         break
#     else:
#         i+=1
#         print ("用户和密码错误，请重新输入！")
#
# print("已错五次，没机会啦~")

# import random
# num1 = random.randint(1,100)
# while True:
#     num2 = int(input("请输入一个数字："))
#     if num1>num2:
#         print("猜小了")
#     elif num1<num2:
#         print("猜大了")
#     else:
#         print("猜对了，游戏结束！")
#         break
# print("生成的随机数是：",num1)


# total = 0
# for i in range(1,101):
#     if i%5==0:
#        total+=i
# print(f"总和为：{total}")


# i = 0
# j = 0
# for k in "aaaahhhhhkkkk":
#     if k=="a":
#         i+=1
#     elif k=="k":
#          j+=1
# print(f"a有{i}个,k有{j}个")







































