# user_weight = float(input("请输入您的体重（单位：千克）："))
# user_height = float(input("请输入您的身高（单位：厘米）："))
# user_BMI = user_weight / user_height ** 2
# print("您的BMI指数为：", str(user_BMI))

# if is_happy:
#     print("开心")
# else
#     print("不开心")

# shopping_list = ["苹果", "香蕉", "橙子", "西瓜"]
# print(len(shopping_list))


# contacts = {"张三": "123456789", "李四": "987654321", "王五": "111111111"}
# contacts.keys()
# contacts.values()
# contacts.items()
# print(str(contacts.items(1)))

# list1 = ["苹果", "香蕉", "橙子", "西瓜"]
# for char in list1:
#     print(char)
#
# for i in range(len(list1)):
#     print(list1[i])
#
# class Student:
#     def __init__(self, name, student_id):
# self.name = name
#         self.student_id = student_id
#
#     def get_name(self):
#         return self.name
#
#     def get_student_id(self):
#         return self.student_id
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_student_id(self, student_id):
#         self.student_id = student_id
#
#     def __str__(self):
#         return "姓名：" + self.name + "，学号：" + str(self.

f = open("./index.html","r",encoding="utf-8")
content = f.read()
print(content)
f.close()