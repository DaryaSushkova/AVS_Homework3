from enum import Enum
from random import randint
from random import uniform
from abc import abstractmethod


class TransportType(Enum):
    """
    Тип транспорта.
    """
    AIRPLANE = 0
    TRAIN = 1
    SHIP = 2


class ShipType(Enum):
    """
    Тип корабля.
    """
    LINER = 0
    TUGBOAT = 1
    TANKER = 2


class Transport:
    """
    Класс, описывающий пассажирский транспорт.
    """
    # Общие параметры.
    speed: int
    distance: float

    def __init__(self, speed, distance):
        """
        Конструктор пассажирского траспорта
        :param speed: скорость транспорта.
        :param distance: расстояние.
        """
        self.speed = speed
        self.distance = distance

    def __str__(self):
        """
        Функция вывода информации об общих параметрах.
        :return: форматируемая строка с информацией.
        """
        return f'speed = {self.speed}, distance = {self.distance}'

    @staticmethod
    def input_file(in_file):
        """
        Функция считывания данных с файла:
        :param in_file: Файл со входными файлами.
        :return: Требуемая функция.
        """
        type_tr = TransportType(int(in_file.readline()))
        if type_tr == TransportType.AIRPLANE:
            return Airplane.input_file(in_file)
        elif type_tr == TransportType.TRAIN:
            return Train.input_file(in_file)
        elif type_tr == TransportType.SHIP:
            return Ship.input_file(in_file)
        else:
            print('Incorrect input data!\n')
            return None

    @staticmethod
    def input_random():
        """
        Функция случайной генерации входных данных.
        :return: Требуемая функция.
        """
        type_tr = TransportType(randint(0, len(TransportType) - 1))
        if type_tr == TransportType.AIRPLANE:
            return Airplane.input_random()
        elif type_tr == TransportType.TRAIN:
            return Train.input_random()
        elif type_tr == TransportType.SHIP:
            return Ship.input_random()
        else:
            return None

    def get_time(self) -> float:
        """
        Функция вычисления времени прохода расстояния.
        :return: Значение времени.
        """
        return self.distance / self.speed

    @abstractmethod
    def output_random(self, input_file):
        """
        Абстрактный метод вывода сгенерированных параметро в файл.
        :param input_file: Выходной файл.
        :return: Строка с данными.
        """
        pass


class Airplane(Transport):
    """
    Класс-наследник, описывающий самолет.
    """
    # Характеристики самолета.
    speed: int
    distance: float
    range_of_flight: int
    lifting_capacity: int

    def __init__(self, speed, distance, range_fl, capacity):
        """
        Конструктор самолета.
        :param speed: Скорость.
        :param distance: Расстояние.
        :param range_fl: Дальность полета.
        :param capacity: Грузоподъемность.
        """
        super().__init__(speed, distance)
        self.range_of_flight = range_fl
        self.lifting_capacity = capacity

    def __str__(self):
        """
        Строковое представление ифнормации о самолете.
        :return: форматируемая строка с информацией.
        """
        return f'Airplane: {super().__str__()}, range = {self.range_of_flight}, ' \
               f'capacity = {self.lifting_capacity}, time = {Transport.get_time(self)}\n'

    @staticmethod
    def input_file(in_file):
        """
        Функция ввода данных о самолете с файла.
        :param in_file: Входной файл.
        :return: Объект самолета.
        """
        str_info = in_file.readline().split()
        speed, distance = int(str_info[0]), float(str_info[1])
        if not speed or not distance:
            print('Incorrect input data!')
            return None
        if speed < 0 or distance < 0:
            print('Incorrect input data!')
            return None
        str_info2 = in_file.readline().split()
        range_fl, capacity = int(str_info2[0]), int(str_info2[1])
        if not range_fl or not capacity:
            print('Incorrect input data!')
            return None
        if range_fl < 0 or capacity < 0:
            print('Incorrect input data!')
            return None
        return Airplane(speed, distance, range_fl, capacity)

    @staticmethod
    def input_random() -> 'Airplane':
        """
        Функция генерации данных самолета.
        :return: Объект самолета.
        """
        speed = randint(1, 25000)
        distance = uniform(1, 50000)
        range_fl = randint(1, 30000)
        capacity = randint(1, 10000)
        return Airplane(speed, distance, range_fl, capacity)

    def output_random(self, input_file):
        """
        Функция вывода в файл сгенерированных данных о самолете.
        :param input_file: Выходной файл.
        :return: Данные о самолете.
        """
        input_file.write(str(TransportType.AIRPLANE.value) + '\n')
        input_file.write(str(self.speed) + ' ')
        input_file.write(str(self.distance) + '\n')
        input_file.write(str(self.range_of_flight) + ' ')
        input_file.write(str(self.lifting_capacity) + '\n')


class Train(Transport):
    """
        Класс-наследник, описывающий поезд.
    """
    # Характеристики поезда.
    speed: int
    distance: float
    count_of_cars: int

    def __init__(self, speed, distance, count):
        """
        Конструктор поезда.
        :param speed: Скорость.
        :param distance: Расстояние.
        :param count: Количество вагонов.
        """
        super().__init__(speed, distance)
        self.count_of_cars = count

    def __str__(self):
        """
        Строковое представление ифнормации о поезде.
        :return: форматируемая строка с информацией.
        """
        return f'Train: {super().__str__()}, cars = {self.count_of_cars}, ' \
               f'time = {Transport.get_time(self)}\n'

    @staticmethod
    def input_file(in_file):
        """
        Функция ввода данных о поезде с файла.
        :param in_file: Входной файл.
        :return: Объект поезда.
        """
        str_info = in_file.readline().split()
        speed, distance = int(str_info[0]), float(str_info[1])
        if not speed or not distance:
            print('Incorrect input data!')
            return None
        if speed < 0 or distance < 0:
            print('Incorrect input data!')
            return None
        cars = int(in_file.readline())
        if not cars:
            print('Incorrect input data!')
            return None
        if cars < 0:
            print('Incorrect input data!')
            return None
        return Train(speed, distance, cars)

    @staticmethod
    def input_random() -> 'Train':
        """
        Функция генерации данных поезда.
        :return: Объект поезда.
        """
        speed = randint(1, 25000)
        distance = uniform(1, 50000)
        cars = randint(1, 50)
        return Train(speed, distance, cars)

    def output_random(self, input_file):
        """
        Функция вывода в файл сгенерированных данных о поезде.
        :param input_file: Выходной файл.
        :return: Данные о поезде.
        """
        input_file.write(str(TransportType.TRAIN.value) + '\n')
        input_file.write(str(self.speed) + ' ')
        input_file.write(str(self.distance) + '\n')
        input_file.write(str(self.count_of_cars) + '\n')


class Ship(Transport):
    """
        Класс-наследник, описывающий корабль.
    """
    # Характеристики корабля.
    speed: int
    distance: float
    displacement: int
    ship_type: ShipType

    def __init__(self, speed, distance, displacement, type_sh):
        """
        Конструктор поезда.
        :param speed: Скорость.
        :param distance: Расстояние.
        :param displacement: Водоизмещение.
        :param type_sh: Тип корабля.
        """
        super().__init__(speed, distance)
        self.displacement = displacement
        self.ship_type = type_sh

    def __str__(self):
        """
        Строковое представление ифнормации о корабле.
        :return: форматируемая строка с информацией.
        """
        return f'Ship: {super().__str__()}, displacement = {self.displacement}, ' \
               f'type = {self.ship_type.name}, time = {Transport.get_time(self)}\n'

    @staticmethod
    def input_file(in_file):
        """
        Функция ввода данных о корабле с файла.
        :param in_file: Входной файл.
        :return: Объект корабля.
        """
        str_info = in_file.readline().split()
        speed, distance = int(str_info[0]), float(str_info[1])
        if not speed or not distance:
            print('Incorrect input data!')
            return None
        if speed < 0 or distance < 0:
            print('Incorrect input data!')
            return None
        str_info2 = in_file.readline().split()
        displacement, type_index = int(str_info2[0]), int(str_info2[1])
        if not displacement or not type_index:
            print('Incorrect input data!')
            return None
        if displacement < 0 or type_index < 0 or type_index > 2:
            print('Incorrect input data!')
            return None
        type_ship = ShipType(type_index)
        return Ship(speed, distance, displacement, type_ship)

    @staticmethod
    def input_random() -> 'Ship':
        """
        Функция генерации данных корабля.
        :return: Объект корабля.
        """
        speed = randint(1, 25000)
        distance = uniform(1, 50000)
        displacement = randint(1, 1000)
        type_ship = ShipType(randint(0, len(ShipType) - 1))
        return Ship(speed, distance, displacement, type_ship)

    def output_random(self, input_file):
        """
        Функция вывода в файл сгенерированных данных о корабле.
        :param input_file: Выходной файл.
        :return: Данные о корабле.
        """
        input_file.write(str(TransportType.SHIP.value) + '\n')
        input_file.write(str(self.speed) + ' ')
        input_file.write(str(self.distance) + '\n')
        input_file.write(str(self.displacement) + ' ')
        input_file.write(str(self.ship_type.value) + '\n')
