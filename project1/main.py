import sys
import time

from container import Container


def help_message():
    """
    Функция вывода инструкции.
    :return: Инструкция.
    """
    print("REQUESTS:\n\n'"
          " -f: specify input and output file\n"
          "format: -f /input_file/ /output_file/\n"
          " -n: random input\n"
          "format: -n /size_of_container/ /file_for_output/\n\n"
          "FORMAT OF INPUT FILE:\n"
          "The first line is the number of elements;\n"
          "The description of each of the elements has the form:\n"
          "The first line is the type of transport: 0 - airplane, 1 - train, 2 - ship;\n"
          "The second line is the general variables: /speed/(integer) /distance/(double)\n"
          "The third line is the characteristics of the element separated by a space:\n"
          "Airplane: /flight_range/(integer) /load_capacity/(integer)\n"
          "Train: /count_of_cars/(integer)\n"
          "Ship: /displacement/(integer) /type/(0 - liner, 1 - tugboat, 2 - tanker)\n")


def error_message1():
    """
    Функция вывода ошибки в командной строке.
    :return: Сообщение.
    """
    print("\nIncorrect command line!\n")


def error_message2():
    """
    Функция вывода ошибки открытия файла.
    :return: Сообщение.
    """
    print("\nFile opening error!\n")


def error_message3():
    """
    Функция вывода ошибки указанной команды.
    :return: Сообщение.
    """
    print("\nThe specified command does not exist!\n")


def main(argv: list):
    """
    Точка входа в программу.
    :param argv: Аргументы командной строки.
    :return: Результат работы программы.
    """
    time_value = time.time()
    help_message()
    if len(argv) != 4:
        error_message1()
        return

    print('Start!\n')
    # Ввод данных из файла.
    if argv[1] == '-f':
        try:
            in_file = open(argv[2], 'r')
            out_file = open(argv[3], 'w')
        except Exception as e:
            print(e)
            error_message2()
            return
        container = Container.input_file(in_file)
        if not container:
            print('Container not generated :(')
            return
        else:
            print('The container has been created!')
        container.output_file(out_file)
        container.straight_selection()
        # Вывод отсортированного контейнера.
        out_file.write('\nSorted transport:\n')
        container.output_file(out_file)
        in_file.close()
        out_file.close()
    # Генерация входных данных.
    elif argv[1] == '-n':
        try:
            count = int(argv[2])
            input_rnd = open(argv[3] + 'random', 'w')
            output_rnd = open(argv[3] + 'out', 'w')
        except:
            error_message2()
            return
        container = Container.input_random(count)
        if not container:
            print('Container not generated :(')
            return
        container.output_random(input_rnd)
        container.output_file(output_rnd)
        # Сортировка контейнера.
        container.straight_selection()
        output_rnd.write('\nSorted transport:\n')
        container.output_file(output_rnd)
        input_rnd.close()
        output_rnd.close()
    else:
        error_message1()
        error_message3()
        return

    print('End\n')
    print(f'Program execution time = {(time.time() - time_value) * 1000} ms')


if __name__ == '__main__':
    main(sys.argv)
