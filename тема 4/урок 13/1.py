# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
import numpy as np
import random

random.randrange(-100, 100)

horizontal = int(input("Количество чисел в строке :"))  # генерация размерности матрицы
vertical = int(input("Количество списков в матрице :"))

matrix_1 = np.array(
    [[random.randrange(-10, 10) for i in range(horizontal)] for i in range(vertical)],
    int,
)
matrix_2 = np.array(
    [[random.randrange(-10, 10) for i in range(horizontal)] for i in range(vertical)],
    int,
)

print(matrix_1 + matrix_2, "Сложил")  # Сложение матрицы
