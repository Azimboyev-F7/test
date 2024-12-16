# Lambda
#
# result = lambda a, b : a + b
#
# print(result(3, 8))



# def func(a, *args, **kwargs):
#     return lambda b : b % a
#
# lam = func(3)
#
# print(lam(8))


# Double
# def func(a, *args, **kwargs):
#     return lambda b : b % a
#
# lam = func(3)
# lam2 = func(4)
#
# print(lam(8))
# print(lam2(16))


# Mini program why we need lambda
# user = int(input("Enter your year :: "))
#
# age = lambda a, b : a - b
#
# print(age(2024, user))                # As you can see that this is a basic syntaxt we don;t need to create def this 1 line code. That's why we need lambda


# class User:
# #     Name = ""
# #     Lastname = ""
# #     Age = ""
# #
# #     def __init__(self, name, lastname, age):
# #         self.Name = name
# #         self.Lastname = lastname
# #         self.Age = age
# #
# #     # def __str__(self):
# #     #     self.Name = name
# #     #     self.Lastname = lastname
# #     #     self.Age = age
# #
# # a = User("Faxriyor", "Azimboyev", 15)
# # print(a)
#     def __init__(self):
#         self.data = {}
#
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
# a = User()
#
# a.data['a'] = 1
# a.data['b'] = 2
# a.__setitem__('a', 3)
# print(a.data)

def lengthOfLastWord(s: str):
        s = s[::]
        print(s)
        # s = len(s)
lengthOfLastWord("Hello world")