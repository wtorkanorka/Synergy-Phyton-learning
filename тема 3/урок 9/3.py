# 3 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
X = list(map(int, input().split()))
Y = set()
for i in X:
    if i in Y:
        print(i, "Yes")
    else:
        Y.add(i)
        print(i, "No")
