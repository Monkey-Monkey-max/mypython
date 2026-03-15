#列表 有序 可重复 可修改

# num_list = []
# for i in range(1,11):
#     num = int(input(f"请输入第{i}个数："))
#     num_list.append(num)
# print(num_list)
# num_list.sort()
# print("排序后的数字列表为：",num_list)
# print(f"最大值为：{max(num_list)}, 最小值为：{min(num_list)},平均值为：{sum(num_list)/len(num_list)}")


# num_list1 = [1,2,3,4,56,7,8]
# num_list2 =[1,2,3,4,5,6]
# list = num_list1+num_list2
# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print (new_list)



# list=[]
# number=0
# for i in range(1,21):
#     number = i**2
#     list.append(number)
# print(list)


# 列表的推导式
# list = [1,2,3,4,5,6,7]
# # new_list = [i**2 for i in list]
# # print(new_list)
# # new_list1 = [i**2 for i in list if i%2==0]
# # print(new_list1)



# list1 = ["Q","W","E"]
# list2 = ["A","S"]
# list3 = ["d","z"]
# list4=[]
# list4=list1+list2+list3
# print(list4)

# list=[1,2,3,4,5,-1,-3,-4,9]
# new_list=[i for i in list if i>0]
# print(new_list)




#字符串 有序 可重复 不可修改
# mail = input("请输入电子邮件：")
# if mail.count("@")==1 and mail.count(".")>=1:
#     print ("邮箱格式正确")
# else:
#     print("邮箱格式错误")


# 回文数
# str = input("请输入一串字符：")
# if str == str[::-1]:
#     print("是回文字")
# else:
#     print("不是回文字")


# list = []
# for k in range(1,5):
#     str = input(f"请输入第{k}个字符串：")
#     str2 = str[::-1].upper()
#     list.append(str2)
# for i in list:
#     print(i,end="")



# 元组 有序 可重复 不可修改
# students = (   ("s001","王林",85,92,78),
#                ("s002","李牧",92,88,95),
#                ("s003","十三",75,85,88),
#                ("s004","增牛",78,85,83),
#                ("s005","王卓",76,82,99)
#          )
# print("学号\t","姓名\t","语文\t","数学\t","英语\t","总分\t","平均分\t")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg =  total/3
#     print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}\t\t")
#
# chinese_score=[s[2] for i in students]
# match_score=[s[3] for i in students]
# Enlish_score=[s[4] for i in students]
# print(f"语文最高分：{max(chinese_score)},语文最低分：{min(chinese_score)},语文平均分:{sum(chinese_score)/len(chinese_score)}")
# print(f"数学最高分：{max(match_score)},数学最低分：{min(match_score)},数学平均分:{sum(match_score)/len(match_score)}")
# print(f"英语最高分：{max(Enlish_score)},英语最低分：{min(Enlish_score)},英语平均分:{sum(Enlish_score)/len(match_score)}")
#
# print("优秀学生名单为：")
#
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg =  total/3
#     if avg >=90:
#         print(f"学生名单有：{s[1]}" ,end="")
#



 # 集合 不可重复，无序，可修改
# football_set = {"王林","曾牛","徐立国"}
# basketball_set = {"王林","张三","李四","王二"}
# french_set = {"许木","十三","韩立","曾牛","张三"}
# art_set = {"紫菱","通天","张三","姜老大"}
#
# print(french_set.intersection(art_set))
# print(french_set & art_set)
#
# print(football_set.intersection(basketball_set).intersection(french_set).intersection(art_set))
# print(football_set & basketball_set & french_set & art_set)
#
# print(football_set.difference(basketball_set))
# print(football_set - basketball_set)
#
# all_set = football_set | basketball_set | french_set | art_set
# all_tuple = [*football_set,*basketball_set,*french_set,*art_set]
# for s in all_set:
#     print(f"{s}选修了{all_tuple.count(s)}个课")

# 字典 key不能重复，且不可变类型。可修改，不能索引，只能由key找value

# dict1 = {"王林":670,"李慕婉":608,"徐立国":580,"韩立":688}
# print(dict1)
#
# #添加
# dict1["涛哥"] = 550
# print(dict1)
# #修改
# dict1["涛哥"] = 600
# #查询
# print(dict1["涛哥"])
# print(dict1.get("涛哥"))
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# #删除
# score=dict1.pop("徐立国")
# print(score)
# print(dict1)
#
# del dict1["涛哥"]
# print(dict1)
#
# #遍历
# for s in dict1.keys():
#     print(f"{s}:{dict1[s]}")


#购物系统
print("欢迎来到购物车~")
name="""
#################################
#            1.添加购物车         #
#            2.修改购物车         #
#            3.删除购物车         #
#            4.查询购物车         #
#            5.退出购物车         #
#################################
"""
shopping_car={"宝宝霜":{"商品价格":30,"商品数量":2},
              "洗发水":{"商品价格":50,"商品数量":7}}
while True:
    print(name)
    choice = input("请输入你的选项：")
    match choice:
         case "1":
             good_name =input("请输入商品名称：")
             good_price = float(input("请输入价格："))
             good_number = int(input("请输入商品数量："))
             if good_name in shopping_car:
                 print ("商品已存在")
             else:
                 shopping_car[good_name] = {"商品价格":good_price,"商品数量":good_number}  #添加商品
                 print("添加成功")
         case "2":
            good_name = input("请输入修改商品名称：")
            good_price = float(input("请输入修改价格"))
            good_number = int(input("请输入修改商品数量："))
            if good_name not in shopping_car:
                print("商品不存在")
            else:
                shopping_car[good_name] = {"商品价格": good_price, "商品数量": good_number}
                print("修改成功")
         case "3":
            good_name = input("请输入删除商品名称：")
            if good_name not in shopping_car:
                print("商品不存在")
            else:
                del  shopping_car[good_name]
                print("删除成功")
         case "4":
             for s in shopping_car.keys():
                 print(f"商品名称：{[s]},{shopping_car[s]}")
         case "5":
             print("退出购物车")
             break































































