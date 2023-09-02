# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
N = int(input())
equal = 0
for i in range(N):
    x = int(input())
    if x == 0:
        equal += 1
print("Количество нулей: ", equal)
