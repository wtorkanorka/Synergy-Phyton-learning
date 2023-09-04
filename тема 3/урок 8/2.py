# 2 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
N = int(input())
arr = []
for i in range(N):
    x = int(input())
    arr.append(x)
lastElement = arr.pop()
arr.insert(0, lastElement)
print(arr)
