from datetime import date, datetime
from checks import check_date


def menu(info, commands):
    choice = ''
    while choice not in commands:
        print(info)
        choice = input('Введите цифру: ')
        if choice in commands:
            return choice
        else:
            print('Такой команды нет, попробуйте еще раз...')


def create_animal():
    commands = []
    correct_date = []
    command = 0
    year = 0
    month = 0
    day = 0
    years, months, days = check_date()
    name = input('Введите имя: ')
    while command != '1':
        command = input('Введите комманды, которые питомец исполняет:\n'
                        '1 - далее: ')
        if len(command) != 0 and ' ' not in command and not command.isdigit():
            commands.append(command.strip())
    while year not in years:
        year = input('Введите год рождения в формате "YYYY" и диапозоне 50 ближайших лет : ')
        if year in years:
            correct_date.append(year)
        else:
            print('Неверный формат или диапозон.')
    while month not in months:
        month = input('Введите месяц рождения в формате "MM": ')
        if month in months:
            correct_date.append(month)
        else:
            print('Неверный формат')
    while day not in days:
        day = input('Введите день рождения в формате "DD": ')
        if day in days:
            correct_date.append(day)
        else:
            print('Неверный формат')
    birthdate = date(int(correct_date[0]), int(correct_date[1]), int(correct_date[2]))
    return [name, commands, birthdate]
