# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


from games import sem6_home2_chess as chs

QUEENS_NUMBER = 8
NUMBER_OF_SET = 4

count = 0
dic_queens = {}

while count != NUMBER_OF_SET:
    queens = chs.queens_setup(QUEENS_NUMBER)
    while not chs.check(queens):
        # print(res)
        queens = chs.queens_setup(QUEENS_NUMBER)
    count += 1
    dic_queens[count] = queens

print(dic_queens)

