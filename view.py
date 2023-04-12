

def show_all(list_animals):
    i = 1
    for animal in list_animals:
        print(f'{i} - {animal}')
        i += 1


def write_animals(animal_list):
    with open('animals.txt', 'w', encoding='utf-8') as file:
        for animal in animal_list:
            file.write(animal + '\n' )


def prepare_animal_format(data):
    category, animal_type, name, commands, birthdate = data.split(';')
    data_dict = {'Категория': category,
                 'Вид животного': animal_type,
                 'Имя': name,
                 'Команды': str(commands),
                 'Дата рождения': str(birthdate)}
    return data_dict


def read_animals():
    list_animals = []
    with open('animals.txt', 'r', encoding='utf-8') as file:
        for f in file:
            if f != [' ', '', '\n']:
                list_animals.append(f.strip())
        return list_animals
