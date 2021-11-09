from transport import Transport

# Максимально возможный размер контейнера.
MAX_LENGTH = 10000


class Container:
    """
    Класс, описывающий контенйер.
    """
    # Список транспорта
    transports: list

    def __init__(self):
        """
        Конструктор контейнера.
        """
        self.transports = list()

    def __str__(self):
        """
        Строковое представление контейнера.
        :return: Форматируемая строка с информацией.
        """
        return f'{len(self.transports)} transports:\n'

    def add_transport(self, transport) -> bool:
        """
        Функция добавления транспорта в контейнер.
        :param transport: Объект транспорта.
        :return: Удалось ли добавить элемент.
        """
        if len(self.transports) >= MAX_LENGTH:
            print('You can not add an element, the container is full!')
            return False
        else:
            self.transports.append(transport)
            return True

    @staticmethod
    def input_file(in_file):
        """
        Функция ввода информации из файла.
        :param in_file: Входной файл.
        :return: Заполненный контейнер.
        """
        container = Container()
        count_str = in_file.readline()
        if not count_str:
            return None
        # Блок с учетом возникновения исключения при чтении с файла.
        try:
            count = int(count_str)
            if count < 0 or count > 10000:
                print('Incorrect count of transport!')
                return None
            for index in range(0, count):
                if not container.add_transport(Transport.input_file(in_file)):
                    break
            return container
        except ValueError:
            print('File reading error!')
            return None

    @staticmethod
    def input_random(count):
        """
        Функция ввода сгенерированных данных.
        :return: Заполненный контейнер.
        """
        container = Container()
        if count < 0 or count > 10000:
            print('The size of the container must be at least 0 and not more than 10000!')
            return None
        for index in range(count):
            container.add_transport(Transport.input_random())
        return container

    def output_file(self, out_file):
        """
        Функция вывода информации о контейнере.
        :param out_file: Выходной файл.
        :return: Результат вывода.
        """
        out_file.write(str(self))
        for index in range(0, len(self.transports)):
            out_file.write(f'{index + 1}: ' + str(self.transports[index]))

    def output_random(self, random_file):
        """
        Функция вывода сгенерированных данных.
        :param random_file: Выходной файл.
        :return: Результата вывода.
        """
        random_file.write(str(len(self.transports)) + '\n')
        for transport in self.transports:
            transport.output_random(random_file)

    def straight_selection(self):
        """
        Функция сортировки элементов контейнера с помощью прямого выбора.
        :return: Результат сортировки.
        """
        for i in range(0, len(self.transports) - 1):
            temporary = self.transports[i]
            for j in range(i + 1, len(self.transports)):
                if self.transports[j].get_time() > self.transports[i].get_time():
                    temporary = self.transports[i]
                    self.transports[i] = self.transports[j]
                    self.transports[j] = temporary
