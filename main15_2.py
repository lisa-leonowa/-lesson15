import logging
import argparse

"""
Урок 4, задача 1.
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, 
и возвращает транспонированную матрицу.
"""


def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    try:
        for row in range(rows):
            for col in range(cols):
                transposed[col][row] = matrix[row][col]
    except IndexError as e:
        logger.info(f'При транспонировании матрицы было вызвано исключение: {e}\n'
                    f'Вероятно, возможно не все элементы матрицы были указаны! В результате работы программы '
                    f'будет возвращена входная матрица!')
        print("Вероятно, возможно не все элементы матрицы были указаны! "
              "В результате работы программы будет возвращена входная матрица!")
        return matrix
    return transposed


if __name__ == "__main__":
    logging.basicConfig(filename='Log/log_for_main15_2.log',
                        filemode='w',
                        format='{levelname} - {asctime} функция "{funcName}()" строка {lineno} :\n{msg}\n',
                        encoding='utf-8',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Вариант запуска через консоль
    parser = argparse.ArgumentParser(description='Транспонирование матрицы. Для работы укажите матрицу из целых чисел, '
                                                 'которую хотите транспонировать!')
    parser.add_argument('-row', type=int)
    parser.add_argument('-col', type=int)
    parser.add_argument('-matrix', type=str)
    try:
        args = parser.parse_args()
        temporary = args.matrix.split()
        matrix = []
        counter = 0
        for i in range(int(args.row)):
            matrix_temporary = []
            for j in range(int(args.col)):
                matrix_temporary.append(float(temporary[counter]))
                counter += 1
            matrix.append(matrix_temporary)
        print('Исходная матрица')
        print(*matrix, sep='\n')
        transposed_matrix = transpose(matrix)
        print('Транспонированная матрица')
        print(*transposed_matrix, sep='\n')
    except Exception as e:
        logger.info(f'При транспонировании матрицы было вызвано исключение: {e}')
        print("Вероятно, не все аргументы были указаны! ")

    # Запуски командной строкой:
    # python main15_2.py -row=3 -col=3 -matrix="1 2 3 4 5 6 7 8 9"
    # python main15_2.py -row=4 -col=2 -matrix="1 2 3 4 5 6 7 8"
    # python main15_2.py -row=2 -col=5 -matrix="1 2 3 4 5 6 7 8 9 10"

    # Второй вариант запуска через IDLE
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]
    # print('Исходная матрица')
    # print(*matrix, sep='\n')
    # transposed_matrix = transpose(matrix)
    # print('Транспонированная матрица')
    # print(*transposed_matrix, sep='\n')
