# 1.	Создайте lambda-функцию для нахождения подстроки в введённой строке.
print("Задание 1")
f = lambda str, txt: txt if txt in str else "txt is not in str"
print(f("Just some string", "Just"))
print("_______________")
# Не совсем поняла, стоило вывести True / False или само подстроку. Поэтому вывела подстроку, если она есть

# 2.	Проверьте число на чётность с помощью анонимной функции.
print("Задание 2")
f = lambda is_odd: is_odd % 2 == 0
print(f(5))
print("_______________")

# 3.	Напишите lambda-функцию, которая будет приветствовать пользователя имя которого введено корректно, с большой буква.
# Иначе будет выводить сообщение о неверно введённом имени.
print("Задание 3")
f = lambda \
        name_for_greeting: f"Hello, {name_for_greeting}!" if name_for_greeting.istitle() else "The name is incorrect :("
print(f("Marina"))
print("_______________")

# 4.	Напишите рекурсивную функцию digits(n), которая принимает натуральное число и возвращает строку с цифрами
# этого числа справа налево, разделяя их пробелами.
print("Задание 4")


def digits(n):
    """
    Функция принимает натуральное число и возвращает строку с цифрами этого числа справа налево, разделяя их пробелами.
    Args:
        n: любое натуральное число
    Returns: строка с цифрами натурального числа справа налево, разделенная пробелами
    """
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + ' ' + digits(n // 10)


print(digits(10225))
print("_______________")

# 5.	Напишите рекурсивную функцию is_power(n), которая возвращает True,
# если переданное натуральное число является степенью двойки, и False иначе.
# Sample Input:
# 1048576
# Sample Output:
# True
print("Задание 5")


def is_power(n: int) -> int:
    """
    Функция возвращает True, если переданное натуральное число является степенью двойки, и False иначе.
    Args:
        n: целое число.
    Returns: целое число.
    """
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power(n // 2)
    else:
        return False


print(is_power(1048576))
print("_______________")

# 6.	Дано натуральное число N. Вычислите сумму его цифр
# Sample Input:
# 14623
# Sample Output:
# 16
print("Задание 6")


def sum_of_digits(n: int) -> int:
    """
    Функция вычисляет сумму цифр натурального числа.
    Args:
        n: натуральное число.
    Returns: целое число.
    """
    if n > 9:
        return n % 10 + sum_of_digits(n // 10)
    else:
        return n


print(sum_of_digits(14623))
print("_______________")

# 7.	Дана функция, которая выводит все простые числа в промежутке от 1 до 100.
# Написать декоратор который будет проверять время работы этой функции. Задекорировать функцию.
# Вывести вpемя работы этой функции, а так же сами простые числа.
print("Задание 7")
import time


def time_of_function(func):
    """
    Функция возвращает время работы другой функции в наносекундах.
    """

    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print(f"Function time is: {time.perf_counter_ns() - start_time} ns")
        return res

    return wrapped


@time_of_function
def find_primes():
    """
    Функция выводит все простые числа в промежутке от 1 до 100.
    """
    primes = []
    for num in range(2, 100):
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes


print(find_primes())
print("_______________")

# 8.	Дана функция, которая проверяет введённый пользователем пароль. Задекорировать её так,
# чтобы при правильно введённом пароле она приветствовала пользователя.
print("Задание 8")


def greet_if_pwd_correct(func):
    """
    Функция приветствует пользователя, если пароль введен корректно.
    """
    def wrapper():
        func()
        print("Добро пожаловать!")
    return wrapper


@greet_if_pwd_correct
def check_pwd():
    """
    Функция проверяет на правильность пароль, введенный пользователем.
    """
    pwd = (input("Введите пароль: "))
    while pwd != "test":
        print("Пароль неверный!")
        pwd = input("Введите пароль еще раз: ")
    print("Пароль верный!")


check_pwd()
print("_______________")

# 9.	*Дано натуральное число n>1. Выведите все простые делители этого числа в порядке не убывания с учетом кратности.
# Используйте рекурсию!
# 18
# Sample Output:
# 2 3 3
print("Доп задание 9")


def prime_factor(n: int, a=2, res=[]):
    """
    Функция выводит все простые делители этого числа в порядке возрастания с учетом кратности.
    Args:
        n: натуральное число.
        a: необязательный аргумент функции.
        res: необязательный аргумент функции.

    Returns:

    """
    if n < a * a:
        print(res + [n])
        return
    if n % a == 0:
        return prime_factor(n // a, a, res + [a])
    else:
        return prime_factor(n, a + 1, res)


prime_factor(18)
