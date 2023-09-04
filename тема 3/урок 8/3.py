# 3 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
m = int(input("Максимальная масса удержания лодки на воде :"))
n = int(input("Количество рыбаков :"))
massOfFisherman = []


for i in range(n):
    x = int(input(f"Вес рыбака №{i + 1} :"))
    massOfFisherman.append(x)


def minimum_boats(m, n, weights):
    weights.sort()  # Сортируем веса рыбаков по возрастанию
    boats = 0  # Счетчик лодок
    i = 0  # Индекс первого рыбака
    j = n - 1  # Индекс последнего рыбака

    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1  # Переправляем первого и последнего рыбаков вместе
        j -= 1  # Переправляем последнего рыбака отдельно
        boats += 1  # Увеличиваем количество лодок

    return boats


boats = minimum_boats(m, n, massOfFisherman)
print(
    f"Максимальная масса удержания лодки на воде : {m},",
    f"Количество рыбаков : {n},",
    f"Массы рыбаков : {list(massOfFisherman)},",
    f"Количество лодок : {boats}",
)
