# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_elements(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_elements(lst, index + 1)
    else:
        print("Конец списка")


print_elements(my_list)
