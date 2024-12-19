import random
# Единственное использование списков, для оптимизации кода
cards_description = [
    "Использовать оружие",
    "Защита +3 SEC",
    "Снести в два раза меньше урона и получить 3 защиты",
    "Снести в два раза больше урона, но потерять всю защиту",
    "Использовать оружие",
    "Потерять 2 HP, но получаете 15 защиты",
    "Получить +5 SEC, но враг получает +2 HP",
    "Использовать оружие",
    "Использовать оружие",
    "Использовать оружие"
]
# Функции
def fight(enemy_name, hp_enemy, boss, max_damage=1):
    global hp, part, special_cards, gun_damage, balance, cards_description
    secure_clear = True
    while hp_enemy > 0 and hp > 0:
        if secure_clear:
            sec = 0
        energy = 3
        hp_enemy_emoji = ''
        hp_emoji = ''
        for i in range(int(hp_enemy)):
            hp_enemy_emoji += '❤️'
        for i in range(hp):
            hp_emoji += '❤️'
        for i in range(3 - hp):
            hp_emoji += '🤍'
        print(f"🗡️ | Враг: {enemy_name}\n"
              f"❤️ | Ваше здоровье: {hp_emoji}\n"
              f"🛡️ | Защита: {sec}\n"
              f"👿 | Здоровье врага: {hp_enemy_emoji}\n")
        cards = ''
        for i in range(3):
            if random.randint(1, 5) == 1 and special_cards != '':
                card = f"{random.choice(special_cards)}"
                if card == 'A':
                    card_desc = "Либо умираете вы, либо враг"
                elif card == 'B':
                    card_desc = "Защита не пропадает в конце вашего хода"
                elif card == 'C':
                    card_desc = "Востановить все здоровье"
                elif card == 'D':
                    card_desc = "Убежать от врага"
                elif card == 'E':
                    card_desc = "Снести 10 урона"
                elif card == 'F':
                    card_desc = "Получить 3 HP"
                card_desc += " (одноразовая карта)"
            else:
                card = str(random.randint(0, 9))
                card_desc = cards_description[int(card)]
            if i == 0:
                card_1 = card
                card_desc_1 = card_desc
            elif i == 1:
                card_2 = card
                card_desc_2 = card_desc
            elif i == 2:
                card_3 = card
                card_desc_3 = card_desc
        for i in range(1):
            print(f"🃏 | Выберите карту:\n"
                  f"1 - {card_desc_1}\n"
                  f"2 - {card_desc_2}\n"
                  f"3 - {card_desc_3}")
            card = int(input('Введите номер (1-3): '))
            if card == 1:
                card_active = card_1
            elif card == 2:
                card_active = card_2
            else:
                card_active = card_3
            # Действие карты
            if card_active == 'A':
                if random.randint(1, 2) == 1:
                    hp = 0
                    print("Вы умерли...")
                    exit("Dead")
                else:
                    hp_enemy = 0
                    print("Враг умер...")
                    special_cards = special_cards.replace(card_active, '')
                    return
            elif card_active == 'B':
                secure_clear = False
                special_cards = special_cards.replace(card_active, '')
            elif card_active == 'C':
                hp = 3
                special_cards = special_cards.replace(card_active, '')
            elif card_active == 'D':
                special_cards = special_cards.replace(card_active, '')
                if boss:
                    print("От босса нельзя убежать!")
                else:
                    return
            elif card_active == 'E':
                hp_enemy -= 10
                special_cards = special_cards.replace(card_active, '')
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == 'F':
                hp = 3
                special_cards = special_cards.replace(card_active, '')
            elif card_active == '0':
                hp_enemy -= gun_damage
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == '1':
                sec += 3
            elif card_active == '2':
                hp_enemy -= int(gun_damage / 2)
                sec += 3
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == '3':
                hp_enemy -= gun_damage * 1.25
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
                sec = 0
            elif card_active == '4':
                hp_enemy -= gun_damage
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == '5':
                hp -= 2
                sec += 15
            elif card_active == '6':
                sec += 5
                hp_enemy += 2
            elif card_active == '7':
                hp_enemy -= gun_damage
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == '8':
                hp_enemy -= gun_damage
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
            elif card_active == '9':
                hp_enemy -= gun_damage
                print(f"Вы нанесли {gun_damage} урона врагу! Его здоровье: {hp_enemy}")
        # Ход врага
        for i in range(random.randint(1, max_damage)):
            if sec > 0:
                sec -= 1
                print(f"Удар врага отражен! Ещё защиты: {sec}")
            else:
                if random.randint(1, 2) == 1:
                    hp -= 1
                    print(f"{enemy_name} бьет ваc! -1HP | Ваше здоровье: {hp}")
                else:
                    print(f"{enemy_name} не попал!")
        if hp < 1:
            print("-" * 16)
            print("| Вы умерли... |")
            print("-" * 16)
            exit("Dead")
        if hp_enemy < 1:
            if not boss:
                print("\nВы убили врага!")
                if boss:
                    hp_old = hp
                    hp = 3
                    balance_old = balance
                    balance +=  random.randint(2500, 3000)
                else:
                    hp_old = hp
                    hp += 1
                    if hp > 3:
                        hp = 3
                    balance_old = balance
                    balance += random.randint(500, 1000)
                print(f"Вот ваши улучшения:\n"
                      f"❤️ | Здоровье: {hp_old} -> {hp}\n"
                      f"💵 | Баланс: {balance_old} -> {balance}")
                special_choice = ['A', 'B', 'C', 'D', 'E']
                for i in range(3):
                    card = random.choice(special_choice)
                    if i == 0:
                        card_special_choice_1 = card
                        if card == 'A':
                            card_desc_1 = "Либо умираете вы, либо враг"
                        elif card == 'B':
                            card_desc_1 = "Защита не пропадает в конце вашего хода"
                        elif card == 'C':
                            card_desc_1 = "Востановить все здоровье"
                        elif card == 'D':
                            card_desc_1 = "Убежать от врага"
                        elif card == 'E':
                            card_desc_1 = "Снести 10 урона"
                        elif card == 'F':
                            card_desc_1 = "Получить 3 HP"
                    elif i == 1:
                        card_special_choice_2 = card
                        if card == 'A':
                            card_desc_2 = "Либо умираете вы, либо враг"
                        elif card == 'B':
                            card_desc_2 = "Защита не пропадает в конце вашего хода"
                        elif card == 'C':
                            card_desc_2 = "Востановить все здоровье"
                        elif card == 'D':
                            card_desc_2 = "Убежать от врага"
                        elif card == 'E':
                            card_desc_2 = "Снести 10 урона"
                    elif i == 2:
                        card_special_choice_3 = card
                        if card == 'A':
                            card_desc_3 = "Либо умираете вы, либо враг"
                        elif card == 'B':
                            card_desc_3 = "Защита не пропадает в конце вашего хода"
                        elif card == 'C':
                            card_desc_3 = "Востановить все здоровье"
                        elif card == 'D':
                            card_desc_3 = "Убежать от врага"
                        elif card == 'E':
                            card_desc_3 = "Снести 10 урона"
                        elif card == 'F':
                            card_desc_3 = "Получить 3 HP"
                print("А также, вы можете выбрать новую специальную карту в свой набор, "
                      "её можно использовать только один раз.")
                print(f"1 - {card_desc_1}\n"
                      f"2 - {card_desc_2}\n"
                      f"3 - {card_desc_3}")
                sp_var = int(input('Введите номер (1-3): '))
                if sp_var == 1:
                    special_cards += card_special_choice_1
                elif sp_var == 2:
                    special_cards += card_special_choice_2
                else:
                    special_cards += card_special_choice_3
                return

# Игра
while True:
    part = 1
    while part == 1:
        person = 0
        gun = 0
        hp = 3
        sec = 3
        balance = 0
        special_cards = ''
        print("Добро пожаловать в игру, путник!\n"
              "Выберите персонажа:\n"
              "1 - Воин | 2 - Стрелок | 3 - Маг | 4 - Самурай")
        person = int(input('Введите номер (1-4): '))
        if person in [1, 2, 3, 4]:
            print("Хороший выбор!")
            print("Теперь выберите оружие:")
            if person == 1:
                print("1 - Palka | 2 - Меч | 3 - Нож | 4 - Без оружия")
            elif person == 2:
                print("1 - Пистолет | 2 - Автомат | 3 - Дробовик | 4 - Без оружия")
            elif person == 3:
                print("1 - Волшебная палочка | 2 - Посох | 3 - Волшебный лук | 4 - Без оружия")
            elif person == 4:
                print("1 - Катана | 2 - Костяной клинок | 3 - Маска | 4 - Без оружия")
            gun = int(input('Введите номер (1-4): '))
            if gun in [1, 2, 3, 4]:
                if person == 1:
                    person_name = "Войн"
                    if gun == 1:
                        gun_name = "Палка"
                        gun_damage = 1
                    elif gun == 2:
                        gun_name = "Меч"
                        gun_damage = 2
                    elif gun == 3:
                        gun_name = "Нож"
                        gun_damage = 3
                    elif gun == 4:
                        gun_name = "Без оружия"
                        gun_damage = 0
                elif person == 2:
                    person_name = "Стрелок"
                    if gun == 1:
                        gun_name = "Пистолет"
                        gun_damage = 1
                    elif gun == 2:
                        gun_name = "Автомат"
                        gun_damage = 2
                    elif gun == 3:
                        gun_name = "Дробовик"
                        gun_damage = 3
                    elif gun == 4:
                        gun_name = "Без оружия"
                        gun_damage = 0
                elif person == 3:
                    person_name = "Маг"
                    if gun == 1:
                        gun_name = "Волшебная палочка"
                        gun_damage = 1
                    elif gun == 2:
                        gun_name = "Посох"
                        gun_damage = 2
                    elif gun == 3:
                        gun_name = "Волшебный лук"
                        gun_damage = 3
                    elif gun == 4:
                        gun_name = "Без оружия"
                        gun_damage = 0
                elif person == 4:
                    person_name = "Самурай"
                    if gun == 1:
                        gun_name = "Катана"
                        gun_damage = 1
                    elif gun == 2:
                        gun_name = "Костяной клинок"
                        gun_damage = 2
                    elif gun == 3:
                        gun_name = "Маска"
                        gun_damage = 3
                    elif gun == 4:
                        gun_name = "Без оружия"
                        gun_damage = 0
                print(f"🥷 | Персонаж: {person_name}\n"
                      f"🗡️ | Оружие: {gun_name}\n"
                      f"💣 | Множитель урона: {gun_damage}")
                print("1 - Выбрать сложность | 2 - Начать заново")
                var = int(input('Введите номер (1-2): '))
                if var == 1:
                    print("\nВыберите сложность:\n"
                          "1 - Легкая | 2 - Сложная")
                    var = int(input('Введите номер (1-2): '))
                    if var == 1:
                        gun_damage *= 1.25
                    part = 2
                    break
        else:
            print("Вы думаете, тут будет секрета? Нет, не будет.")
            input("--- Нажмите Enter для продолжения ---")
    while part == 2:
        print('\n'*10)
        print("--- 1 ЧАСТЬ ---")
        print("""
        Лихие времена настали для королевства Эльтария. Туманные предвестия войны 
        висят в воздухе, а торговые пути перекрыты загадочными силами. 
        Перед вами открыты древние доспехи, сверкающие мечи и шепчущие книги заклинаний.
        Ваш путь начинается с предельной тишины лесной долины. Лишь шум ручья и пенье птиц 
        перебивают стук вашего сердца. Неведомая сила зовет вас вглубь, на встречу с первым испытанием.
        """)
        input("--- Нажмите Enter для продолжения ---")
        part = 3
    while part == 3:
        print('\n'*10)
        print("--- 2 ЧАСТЬ ---")
        print("Ваш путь начинается с предельной тишины лесной долины. Лишь шум ручья и пенье птиц "
              "перебивают битье вашего сердца. Неведомая сила зовет вас вглубь, на встречу с первым испытанием.")
        input("Enter - Начать битву")
        fight("Слизнь", 2, False, 1)
        print("Отличная работа! Вы можете получить приз, если отнесете тело слизня охотнику.")
        part = 31
    while part == 31:
        print("1 - Отнести тело слизня | 2 - Искать ещё врагов | 3 - Пойти дальше")
        var = int(input('Введите номер (1-2): '))
        if var == 1:
            print("Вы несли тело слизня, но тут вам стало плохо, начала кружить1ёся голова.")
            print("1 - Выбросить слизня | 2 - Продолжить нести (может снять урон)")
            var = int(input('Введите номер (1-2): '))
            if var == 1:
                print("И тут, он резко ожил! Вы начали с ним драться!")
                fight("Слизнь", 2, False, 1)
                print("Вы вроде победили слизня, но резко потеряли сознание. Очнувшись, вы опять увидели мертвого"
                      "слизня.")
            else:
                for i in range(3):
                    if hp < 1:
                        print("Вы умерли, похоже слизнь всё таки был жив, и вы зря продолжили нести.")
                    if random.randint(1, 3) != 1:
                        print("-1 HP, точно продолжить нести?")
                        hp -= 1
                    else:
                        print("Вам становилось лучше, но вы точно хотите продолжить его нести?")
                    print("1 - Продолжить нести | 2 - Выбросить слизня")
                    var = int(input('Введите номер (1-2): '))
                    if var == 2:
                        print("И тут, он резко ожил! Вы начали с ним драться!")
                        fight("Слизнь", 2, False, 1)
                        print("Вы вроде победили слизня, но резко потеряли сознание. Очнувшись, вы опять увидели мертвого"
                              "слизня.")
                        break
                    print("Вы успешно пренесли слизня, "
                          "но резко потеряли сознание. Очнувшись, вы опять увидели мертвого слизня.")
                    balance += 500
                    break


        elif var == 2:
            while True:
                fight("Неизвестное существо", random.randint(1, 6), False, random.randint(1, 3))
                print("1 - Искать ещё врагов | 2 - Пойти дальше")
                var = int(input('Введите номер (1-2): '))
                if var == 2:
                    part = 4
                    break
            break
        else:
            part = 4
            break
    while part == 4:
        print('\n'*10)
        print("--- 3 ЧАСТЬ ---")
        print("""
        За этими врагами и силами скрываются древние приметы, ведущие к величайшему боссу - 
        Старому Другу, чьи способности выходят за размеры реальности, за исключением вашего воображения.
        """)
        print("1 - Пойти на босса | 2 - Решить не идти")
        var = int(input('Введите номер (1-2): '))
        if var == 1:
            print("Только перед этим надо полечиться и улучшить оружие и карты, вы решаете пойти в магазин.")
            while True:
                print(f"Магазин!\n"
                    f"Баланс - {balance}\n\n"
                    f"1 - Увеличить урон на 1.25 (у вас будет {gun_damage * 1.25})| Цена: {gun_damage * 200}\n"
                    f"2 - Купить карту, которая в бою дает 3 HP (1 шт.) | Цена: 1000\n"
                    f"3 - Аптечка (у вас будет {hp+1}) | Цена: 300\n"
                    f"4 - Получить все специальные карты | Цена: 3500\n"
                    f"5 - Покинуть магазин")
                var = int(input('Введите номер (1-5): '))
                if var == 1 and balance >= gun_damage * 200:
                    gun_damage += 1.25
                    balance -= gun_damage * 200
                elif var == 2 and balance >= 1000:
                    balance -= 1000
                    special_cards += 'F'
                elif var == 3 and balance >= 300:
                    balance -= 300
                    hp += 1
                elif var == 4 and balance >= 3500:
                    balance -= 2000
                    special_cards += 'ABCDE'

                elif var == 5:
                    break
                else:
                    print("Неверный ввод")
            print("Вы вышли из магазина, пора идти к боссу!")
            input("--- Нажмите Enter чтобы встретиться с боссом ---")
            fight("Босс", 15, True, 2)
            print("Вы победили босса, но что теперь?")
            print("После победы над боссом ваш персонаж оказывается на коленях, дыша тяжело после изнурительной битвы."
                  " Перед вами лежит поверженный враг, чья угасающая сила напоминает вам о цене победы."
                  " Свет проникает сквозь листву деревьев, освещая ваш путь к славе и приключениям,"
                  " которые ждут вас впереди. Бесстрашие и решимость, проявленные в этой схватке, сделают ваше"
                  " имя легендарным в этом мире и за его пределами. Ваше приключение только начинается.")
            input("--- Нажмите Enter чтобы продолжить ---")
            for i in range(100):
                if random.randint(1, 2) == 1:
                    print("Назад!")
                else:
                    print("Назад...")
            part = 1
            break
        else:
            print("Вы решили не идти к боссу, но как же так? Вы потратили столько времени...")
            print("Вы решаете вернуться к выбору...")
            input("--- Нажмите Enter чтобы вернуться к выбору ---")