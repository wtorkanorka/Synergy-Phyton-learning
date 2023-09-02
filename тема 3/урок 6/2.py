# 2 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
X = int(input())
delitel = 0
for i in range(1, X + 1):
    if i % 2 == 0:
        delitel += 1
print("Количество делителей: ", delitel)
