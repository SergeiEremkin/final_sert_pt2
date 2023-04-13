

def show_all(list_animals):
    i = 1
    for animal in list_animals:
        print(f'{i} - {prepare_animal_format_to_dicts(animal)}')
        i += 1


def write_animals(animal_list):
    with open('animals.txt', 'w', encoding='utf-8') as file:
        for animal in animal_list:
            file.write(animal + '\n' )


def prepare_animal_format_to_dicts(str_data):
    category, animal_type, name, commands, birthdate = str_data.split(';')
    data_dict = {'Категория': category,
                 'Вид животного': animal_type,
                 'Имя': name,
                 'Команды': commands,
                 'Дата рождения': birthdate}
    return data_dict


def prepare_animal_to_str(dict_data):
    return f"{dict_data['Категория']};{dict_data['Вид животного']};{dict_data['Имя']};{dict_data['Команды']};{dict_data['Дата рождения']}"


def read_animals():
    list_animals = []
    with open('animals.txt', 'r', encoding='utf-8') as file:
        for f in file:
            if f != [' ', '', '\n']:
                list_animals.append(f.strip())
        return list_animals
