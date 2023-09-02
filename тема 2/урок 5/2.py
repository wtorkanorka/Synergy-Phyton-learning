# 2 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
x_1 = list(input())
sogl = 0
a = 0
e = 0
i = 0
o = 0
u = 0


for letter in x_1:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1
    else:
        sogl += 1


complexGlass = a + e + i + o + u
if (a == 0) or (e == 0) or (i == 0) or (o == 0) or (o == 0) or (u == 0):
    print("false")
print(
    "Количество согласных:",
    sogl,
    "Количество гласных:",
    complexGlass,
    "Количество букв a:",
    a,
    "Количество букв e:",
    e,
    "Количество букв i:",
    i,
    "Количество букв o:",
    o,
    "Количество букв u:",
    u,
)
