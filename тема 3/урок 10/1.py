# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
pets = dict()
petName = input("petName :")
animal = input("animal :")
age = input("age :")
lastNumber = int(list(age)[-1])
syntaxAge = ""
if int(age) >= 10 and int(age) < 21:
    syntaxAge = " лет"
elif lastNumber < 5:
    syntaxAge = " года"
elif lastNumber >= 5:
    syntaxAge = " лет"
else:
    syntaxAge = " года"

nameOwner = input("nameOwner :")
pet_info = {
    "Вид питомца": animal,
    "возраст": age + syntaxAge,
    "Имя хозяина": nameOwner,
}
pets[f"{petName}"] = pet_info

print(
    f"Это {pets[petName]['Вид питомца']} по кличке :{petName}, возраст питомца : {pets[petName]['возраст']}, имя владельца : {pets[petName]['Имя хозяина']}"
)
