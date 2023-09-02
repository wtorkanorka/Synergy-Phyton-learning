# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
x_1 = int(input("Введите целое число - "))

if x_1 < 0:
    if x_1 % 2 == 0:
        print("Отрицательное четное число")
    else:
        print("отрицательное нечетное число")
elif x_1 > 0:
    if x_1 % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
elif x_1 == 0:
    print("нулевое число")
