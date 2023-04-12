from interface import menu, create_animal
from models import Dog, Cat, Hamster, Horse, Camel, Donkey, Animals
from view import read_animals, write_animals, show_all, prepare_animal_format


def run():
    choice = 0
    print('Добрый день, рад Вас видеть! Это программа "Реестр домашних животных".\n'
          'Вы можете вести учет животных, добавлять, удалять, просматривать, выводить по ним информацию.')
    print()
    print('Выберите цифру, соответствующую комманде.')
    while choice != '4':
        animal_list = read_animals()
        choice = menu('\n1 - вывести всех животных\n'
                      '2 - добавить животное\n'
                      '3 - детальная информация о животном\n'
                      '4 - выход', ['1', '2', '3', '4'])
        if choice == '1':
            show_all(animal_list)
            detail_choice = menu('Введите номер животного для детальной информации...', [str(i) for i in range(1, len(animal_list))])
            animal = prepare_animal_format(animal_list[int(detail_choice)-1])
            print(animal)
            action_choice = menu('\n1 - редактировать\n'
                                   '2 - удалить\n', ['1', '2'])
            if action_choice == '1':
                pass
            else:
                animal_list.pop(int(detail_choice)-1)
                write_animals(animal_list)

        if choice == '2':
            category = menu('1 - домашнее животное\n'
                            '2 - вьючное животное\n', ['1', '2'])
            if category == '1':
                type_animal = menu('1 - Собака\n'
                                   '2 - Кошка\n'
                                   '3 - Хомяк', ['1', '2', '3'])
                if type_animal == '1':
                    name, commands, birthdate = create_animal()
                    dog = Dog(name, commands, str(birthdate))
                    animal_list.append(str(dog))
                if type_animal == '2':
                    name, commands, birthdate = create_animal()
                    cat = Cat(name, commands, str(birthdate))
                    animal_list.append(str(cat))
                if type_animal == '3':
                    name, commands, birthdate = create_animal()
                    hamster = Hamster(name, commands, str(birthdate))
                    animal_list.append(str(hamster))
            else:
                type_animal = menu('1 - Лошадь\n'
                                   '2 - Верблюд\n'
                                   '3 - Осел', ['1', '2', '3'])
                if type_animal == '1':
                    name, commands, birthdate = create_animal()
                    horse = Horse(name, commands, str(birthdate))
                    animal_list.append(str(horse))
                if type_animal == '2':
                    name, commands, birthdate = create_animal()
                    camel = Camel(name, commands, str(birthdate))
                    animal_list.append(str(camel))
                if type_animal == '3':
                    name, commands, birthdate = create_animal()
                    donkey = Donkey(name, commands, str(birthdate))
                    animal_list.append(str(donkey))
            write_animals(animal_list)
        if choice == '3':
            pass
