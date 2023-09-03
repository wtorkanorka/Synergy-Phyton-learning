# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
word = list(input())
testWord = "".join(word[::-1])
if "".join(word) == testWord:
    print("Yes")
else:
    print("No")
