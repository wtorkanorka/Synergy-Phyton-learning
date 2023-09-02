# 3 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
A = int(input())
B = int(input())
string = ""
for i in range(A, B + 1):
    if i % 2 == 0:
        string = string + str(i) + " "
print(string)
