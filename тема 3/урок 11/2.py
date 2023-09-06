# 2 https://github.com/wtorkanorka/Synergy-Phyton-learning.git

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        },
    },
}


def get_syntax(new_age):
    syntaxAge = ""
    age = int(new_age)
    if age == 1:
        syntaxAge = " год"
    elif 2 <= age <= 4:
        syntaxAge = " года"
    else:
        syntaxAge = " лет"
    return syntaxAge


def create(
    pet_name="default_name",
    pet_type="default_type",
    pet_age="default_age",
    owner_name="default_owner",
):
    new_pet = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name,
    }
    new_pet_name = dict()
    new_pet_name[pet_name] = new_pet
    pets[len(pets) + 1] = dict(new_pet_name)


def read(pet_name):
    ids = list(pets.keys())
    for i in ids:
        if list(pets[i].keys())[0] == pet_name:
            print(pets[i][pet_name], "Возраст бля")
            syntax = get_syntax(pets[i][pet_name]["Возраст питомца"])
            print(syntax, " AAAAAAAAAA")
            print(
                f'Это {pets[i][pet_name]["Вид питомца"]} по кличке "{list(pets[i].keys())[0]}".Возраст питомца:{pets[i][pet_name]["Возраст питомца"]}{syntax}.Имя владельца: {pets[i][pet_name]["Имя владельца"]}'
            )


def update(pet_name):
    ids = list(pets.keys())
    for i in ids:
        pet = pets[i]
        if list(pets[i].keys())[0] == pet_name:
            old_name = list(pets[i].keys())[0]
            pets[i][pet_name]["Вид питомца"] = (
                input("Введите новый вид питомца :") or pets[i][pet_name]["Вид питомца"]
            )

            pets[i][pet_name]["Возраст питомца"] = int(
                input("Введите новый возраст питомца :")
                or pets[i][pet_name]["Возраст питомца"]
            )

            pets[i][pet_name]["Имя владельца"] = (
                input("Введите новое имя владельца :")
                or pets[i][pet_name]["Имя владельца"]
            )
            new_name = input("Введите новое имя питомца :")
            if new_name == "":
                print("Вы не ввели новое имя")
            else:
                pet[new_name] = pet.pop(old_name)


def delete(pet_name):
    ids = list(pets.keys())
    for i in ids:
        if list(pets[i].keys())[0] == pet_name:
            del pets[i]


def list_pets():
    print(pets)


cmd = ""
while cmd != "stop":
    cmd = input()
    if cmd == "create":
        print("Введите Имя питомца, вид, возраст, имя владельца")
        pet_name = input()
        pet_type = input()
        pet_age = input()
        owner_name = input()
        create(pet_name, pet_type, pet_age, owner_name)

    if cmd == "read":
        print("Введите имя питомца, которого хотите получить")
        x = input()
        read(x)
    if cmd == "update":
        pet_name = input("Введите имя питомца :")
        update(pet_name)
    if cmd == "delete":
        pet_name = input("Введите имя питомца, которого хотите удалить из бд :")
        delete(pet_name)
    if cmd == "list":
        list_pets()
