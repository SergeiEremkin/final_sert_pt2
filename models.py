class Animals:
    def __init__(self, name, commands, birthdate):
        self.name = name
        self.commands = commands
        self.birthdate = birthdate

    def __str__(self):
        return f'{self.name};{self.commands};{self.birthdate}'


class Pet(Animals):
    category = 'Домашнее животное'


class PackAnimal(Animals):
    category = 'Вьючное животное'


class Dog(Pet):
    animal_type = 'Собака'

    def __str__(self):
        return f'{self.category};'\
               f'{self.animal_type};'\
               f'{super().__str__()}'


class Cat(Dog):
    animal_type = 'Кошка'

    def __str__(self):
        return super().__str__()


class Hamster(Dog):
    animal_type = 'Хомяк'

    def __str__(self):
        return super().__str__()


class Horse(PackAnimal):
    animal_type = 'Лошадь'

    def __str__(self):
        return f'{self.category};'\
               f'{self.animal_type};'\
               f'{super().__str__()}'


class Camel(Horse):
    animal_type = 'Верблюд'

    def __str__(self):
        return super().__str__()


class Donkey(Horse):
    animal_type = 'Осел'

    def __str__(self):
        return super().__str__()


class IncrementCounter:

    def __init__(self):
        self.value = 0

    def new_value(self):
        self.value += 1
        return self.value

    def __str__(self):
        return f'{self.value}'
