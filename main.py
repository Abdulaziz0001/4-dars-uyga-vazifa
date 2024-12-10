# # 1-misol
# # ------------------------------------------------1-vazifa-------------------------------------------
# class LowercaseDescriptor:
#     def __get__(self, instance, owner):
#         return instance._value.lower()
#
#     def __set__(self, instance, value):
#         instance._value = value.lower()
#
#
# class MyClass:
#     value = LowercaseDescriptor()
#
#     def __init__(self, value):
#         self.value = value
#
#
# obj = MyClass("HELLO")
# print(obj.value)
# obj.value = "WORLD"
# print(obj.value)

# # ------------------------------------------------2-vazifa--------------------------------------------
# class PositiveValueDescriptor:
#     def __get__(self, instance, owner):
#         return instance._value
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Qiymat musbat bo'lishi kerak!")
#         instance._value = value
#
#
# class MyClass:
#     value = PositiveValueDescriptor()
#
#     def __init__(self, value):
#         self.value = value
#
#
# obj = MyClass(10)
# print(obj.value)
# obj.value = -5

# # 2-misol
# # ------------------------------------------------1-vazifa----------------------------------------
# from datetime import datetime, timedelta
#
# today = datetime.today()
#
# seven_days_ago = today - timedelta(days=7)
# seven_days_later = today + timedelta(days=7)
#
# print("Bugungi sana:", today.strftime("%Y-%m-%d"))
# print("7 kun oldin:", seven_days_ago.strftime("%Y-%m-%d"))
# print("7 kun keyin:", seven_days_later.strftime("%Y-%m-%d"))

# # ---------------------------------------------------2-vazifa--------------------------------------
# from datetime import datetime
#
# birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
# today = datetime.today()
#
# age = today.year - birth_year
#
# if today.month == 10 and today.day == 30:
#     print("Tug'ilgan kuningiz bilan!")
# else:
#     print(f"Sizning yoshingiz: {age}")

# # 3-misol
# # ------------------------------------------------------1-vazifa-------------------------------------
# import math
#
# diameter = float(input("Aylananing diametrini kiriting: "))
#
# radius = diameter / 2
#
# area = math.pi * radius ** 2
#
# print(f"Aylana yuzasi: {area:.2f}")

# # ---------------------------------------------------------2-vazifa-------------------------------------
# import math
#
# number = float(input("Sonni kiriting: "))
#
# if number < 0:
#     raise ValueError("Manfiy sonlarning ildizini hisoblash mumkin emas!")
#
# square_root = math.sqrt(number)
# cube_root = number ** (1/3)
#
# print(f"Kvadrat ildiz: {square_root:.2f}")
# print(f"Kub ildiz: {cube_root:.2f}")

# # 4-misol
# import random
#
# integers = [random.randint(1, 100) for _ in range(5)]
#
# floats = [random.uniform(0, 1) for _ in range(3)]
#
# all_numbers = integers + floats
#
# average = sum(all_numbers) / len(all_numbers)
#
# print("Butun sonlar:", integers)
# print("Haqiqiy sonlar:", floats)
# print("Barcha sonlar:", all_numbers)
# print(f"O'rtacha qiymat: {average:.2f}")