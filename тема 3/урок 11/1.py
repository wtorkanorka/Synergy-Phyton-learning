# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
def fac(num):
    if num == 1 or num == 0:
        return 1

    return num * fac(num - 1)


fac_list = []
for i in range(6, 1 - 1, -1):
    fac_list.append(fac(i))
print(fac_list)
