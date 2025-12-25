"""a = int(input("Введите число"))
for a in range(1,a + 1):
    print(a)"""

a1 = int(input("Введите первое число"))
a2 = int(input("Введите второе число"))
if a1 > a2:
    print("Большее число:", a1)
elif a2 > a1:
    print("Большее число:", a2)
else:
    print("Числа равны")