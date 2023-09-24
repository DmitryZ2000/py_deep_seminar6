# sem6_home2
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# sem_home3
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


import random as rnd

def check(my_qeens: tuple) -> True | False:
    """ Проверка на наличие пары, бьющей друг друга"""
    for i in range(len(my_qeens)-1):
        for j in range(i+1, len(my_qeens)):
            if my_qeens[i][0] == my_qeens[j][0] or my_qeens[i][1] == my_qeens[j][1] or \
                abs(my_qeens[i][0]- my_qeens[j][0]) == abs(my_qeens[i][1]-my_qeens[j][1]):
                return False
    return True        


def queens_setup(queens_number: int) -> tuple:
    """ Генерация расстановки ферзей """
    queens_set = set()
    while len(queens_set) < queens_number:
        queens_set.add((rnd.randint(1, 8), rnd.randint(1, 8)))
    return tuple(queens_set)
      
# chess_desk = [[1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0], \
#               [1,0,0,0,0,0,0,0]]

# for i in chess_desk:
#     print(i)



if __name__ == '__main__':
    # queens = ((1, 1), (1, 2), (3, 3), (4, 4), (2, 8), (7, 2), (6, 6), (3, 7))
    # queens = ((2, 4), (5, 5))
    QUEENS_NUMBER = 5
    queens = queens_setup(QUEENS_NUMBER)
    print(queens)
    print(check(queens))



