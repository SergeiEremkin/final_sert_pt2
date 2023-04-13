from interface import menu, create_animal
from models import Dog, Cat, Hamster, Horse, Camel, Donkey, IncrementCounter
from view import read_animals, write_animals, show_all, prepare_animal_format_to_dicts, prepare_animal_to_str


def run():
    counter1 = IncrementCounter()
    choice = 0
    print('Добрый день, рад Вас видеть! Это программа "Реестр домашних животных".\n'
          'Вы можете вести учет животных, добавлять, удалять, просматривать, выводить по ним информацию.')
    print()
    print('Выберите цифру, соответствующую комманде...\n')
    while choice != '3':
        animal_list = read_animals()
        choice = menu('\n1 - вывести всех животных\n2 - добавить животное\n3 - выход', ['1', '2', '3'])
        if choice == '1':
            show_all(animal_list)
            detail_choice = menu('\nВведите номер животного для действия с ним...\n',
                                 [str(i) for i in range(1, len(animal_list))])
            animal = prepare_animal_format_to_dicts(animal_list[int(detail_choice) - 1])
            print(animal)
            action_choice = menu('\n1 - редактировать\n'
                                 '2 - удалить\n'
                                 '3 - назад', ['1', '2', '3'])
            if action_choice == '1':
                change_animal = prepare_animal_format_to_dicts(animal_list.pop(int(detail_choice) - 1))
                print(f"Отредактируйте: Имя, Команды, Дату рождения")
                name, commands, birthdate = create_animal()
                change_animal['Имя'] = name
                change_animal['Команды'] = commands
                change_animal['Дата рождения'] = birthdate
                animal_list.append(prepare_animal_to_str(change_animal))
                write_animals(animal_list)
            if action_choice == '2':
                animal_list.pop(int(detail_choice) - 1)
                write_animals(animal_list)
            if action_choice == '3':
                continue
        if choice == '2':
            try:
                category = menu('1 - домашнее животное\n'
                                '2 - вьючное животное\n', ['1', '2'])
                if category == '1':
                    type_animal = menu('1 - Собака\n'
                                       '2 - Кошка\n'
                                       '3 - Хомяк', ['1', '2', '3'])
                    if type_animal == '1':
                        print(f'\nЗаводим собаку\n')
                        name, commands, birthdate = create_animal()
                        dog = Dog(name, commands, str(birthdate))
                        animal_list.append(str(dog))
                        counter1.new_value()
                    if type_animal == '2':
                        print(f'\nЗаводим кошку\n')
                        name, commands, birthdate = create_animal()
                        cat = Cat(name, commands, str(birthdate))
                        animal_list.append(str(cat))
                        counter1.new_value()
                    if type_animal == '3':
                        print(f'\nЗаводим хомяка\n')
                        name, commands, birthdate = create_animal()
                        hamster = Hamster(name, commands, str(birthdate))
                        animal_list.append(str(hamster))
                        counter1.new_value()
                else:
                    type_animal = menu('1 - Лошадь\n'
                                       '2 - Верблюд\n'
                                       '3 - Осел', ['1', '2', '3'])
                    if type_animal == '1':
                        print(f'\nЗаводим лошадь\n')
                        name, commands, birthdate = create_animal()
                        horse = Horse(name, commands, str(birthdate))
                        animal_list.append(str(horse))
                        counter1.new_value()
                    if type_animal == '2':
                        print(f'\nЗаводим верблюда\n')
                        name, commands, birthdate = create_animal()
                        camel = Camel(name, commands, str(birthdate))
                        animal_list.append(str(camel))
                        counter1.new_value()
                    if type_animal == '3':
                        print(f'\nЗаводим осла\n')
                        name, commands, birthdate = create_animal()
                        donkey = Donkey(name, commands, str(birthdate))
                        animal_list.append(str(donkey))
                        counter1.new_value()
                write_animals(animal_list)
                print(f'В текущей сессии вы завели: {counter1} животных')
            except Exception as err:
                print(f'Что-то пошло не так: {err}')
