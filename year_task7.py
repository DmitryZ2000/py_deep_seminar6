# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

def date_check(date_str: str) -> True | False:
    """Проверка на корректность даты"""
    day, month, year = date_str.split('.')
    MONTH_31 = [1, 3, 5, 7, 8, 10, 12] # Номера месяцев с 31 днем
    MONTH_30 = [4, 6, 9, 11]  # Номера месяцев с 30 днем
    if 1 <= int(year) <= 9999:
        if int(month) in MONTH_31 and 1 <= int(day) <= 31:   
            return True
        elif int(month) in MONTH_30 and 1 <= int(day) <= 30:
            return True
        elif int(month) == 2 and 1 <= int(day) <= 28:
            return True
        elif check_leap_year(int(year)) and int(month) == 2 and int(day) == 29:
            return True           
        else:
            return False
    else:
            return False
    


def check_leap_year(year: int) -> True | False:
    """ Проверка на высокосный год"""
    if year % 4 or (year % 100 == 0 and year % 400): # Скобки можно убрать
        # print('Обычный год')
        return False # Обычный год
    else:
        # print('Высокосный год')
        return True #Высокосный год

if __name__ == '__main__':
    date_str = '29.02.2000'
    print(date_check(date_str))

