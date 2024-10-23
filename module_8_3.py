class Car:
    def __init__(self, model, vin, numbers):
        self.model = model                           # название авто (строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin                        # vin-номер авто (целое число)
        if self.__is_valid_numbers(numbers):
            self.numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):               # номера автомобиля (строка)
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, massage):
        self.massage = massage


class IncorrectCarNumbers(Exception):
    def __init__(self, massage):
        self.massage = massage


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumbers as exc:
    print(exc.massage)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumbers as exc:
    print(exc.massage)
else:
    print(f'{second.model} успешно создан')


try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumbers as exc:
    print(exc.massage)
else:
    print(f'{third.model} успешно создан')
