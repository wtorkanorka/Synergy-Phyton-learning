# 3 https://github.com/wtorkanorka/Synergy-Phyton-learning.git

x = int(input("Минимальная сумма вложения: "))
a = int(input("Количество денег у Майкла: "))
b = int(input("Количество денег и Ивана: "))
if a >= x and b >= x:
    print(2)
elif a >= x and b < x:
    print("Mike")
elif b >= x and a < x:
    print("Ivan")
elif (a + b) >= x:
    print(1)
else:
    print(0)
