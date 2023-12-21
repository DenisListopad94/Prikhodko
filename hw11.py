# 1.	Напишите функцию fib, которая будет выводить последовательно каждое число Фиббоначи.
print("Задание 1")


def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b


for num in fib(10):
    print(num)
print("_______________")

# 2.	Напишите функцию simple, которая будет выводить поочерёдно простые числа от 2 до введённого числа n до вызова исключения.
print("Задание 2")


def simple(n):
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    i = 2
    while i <= n:
        if is_prime(i):
            yield i
        i += 1


for num in simple(20):
    print(num)
print("_______________")

# 3.	Напишите генератор для вывода всех совершенных чисел до 1000000000.
print("Задание 3")


def perfect_numbers(n):
    for num in range(1, n + 1):
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        if num == sum_of_divisors:
            yield num
        if num == 1000000000:
            break


for perfect_number in perfect_numbers(10000):
    print(perfect_number)
print("_______________")

# 4.	Исключить из строки группы символов, расположенные между первыми символами '{' и '}' вместе со скобками.
# Если нет символа '}', то исключить все символы до конца строки после '{'.  Вывести символ, наиболее часто встречающийся в строке.
print("Задание 4")


def remove_bracket_content(s):
    start = s.find('{')
    end = s.find('}')
    if start != -1:
        if end != -1:
            s = s[:start] + s[end + 1:]
        else:
            s = s[:start]
    return max(s, key=s.count), s


test_str = "abc{def}ghi"
most_common_char, modified_str = remove_bracket_content(test_str)
print("Наиболее частый символ:", most_common_char)
print("Измененная строка:", modified_str)
print("_______________")

# 5.	Ваш отдел работает над приложением, обращающимся к некоторому серверу. Вам поручили реализовать некоторые запросы: GET, POST и DELETE. В контексте вашего приложения POST-запрос добавляет строку на сервер, GET-запрос возвращает последнюю добавленную строку, а DELETE-запрос удаляет последнюю добавленную строку. Дан список команд с запросами (GET и DELETE не принимают параметров, а POST принимает строку или число), список команд прерывается точкой. Выведите, что возвращает сервер, а также строки, которые остались в списке, разделяя их через пробел.
# Sample Input:
# POST 12
# POST 15
# POST 81
# GET
# DELETE
# DELETE
# POST Stack Overflow
# POST Recursion
# DELETE
# GET
# .
# Sample Output:
# 81
# Stack Overflow
print("Задание 5")


def simulate_server(commands):
    stack = []
    output = []

    for command in commands:
        if command.startswith("POST"):
            _, value = command.split(maxsplit=1)
            stack.append(value)
        elif command == "GET" and stack:
            output.append(stack[-1])
        elif command == "DELETE" and stack:
            stack.pop()

    return output, " ".join(stack)


commands = [
    "POST 12", "POST 15", "POST 81", "GET", "DELETE",
    "DELETE", "POST Stack Overflow", "POST Recursion", "DELETE", "GET", "."
]
server_output, remaining_stack = simulate_server(commands[:-1])
print("Возвращаемые значения:", server_output)
print("Оставшиеся строки:", remaining_stack)
print("_______________")

# 6.	Используя list comprehension. Сгенерируйте список как показано ниже:
# 1    1    1    1     1    1
# 1    2    3    4     5    6
# 1    3    6   10  15    21
# 1   4   10   20  35    56
# 1   6   21   56  126  252
print("Задание 6")
list_comprehension = [[sum(range(1, j + 1)) for j in range(i + 1)] for i in range(6)]
for row in list_comprehension:
    print(row)
print("_______________")

# 7.	Коля понял, что у многих из его знакомых есть несколько телефонных номеров и нельзя хранить только один из них.
# Он попросил доработать Вашу программу так, чтобы можно было добавлять к существующему контакту новый номер или даже несколько номеров, которые передаются через запятую.
#  По запросу телефонного номера должен выводиться весь список номеров в порядке добавления, номера должны разделяться запятой.
#  Если у контакта нет телефонных номеров, должна выводиться строка "Не найдено".
# Sample Input:
# Ben 89001234050, +70504321009
# Alice 210-220
# Alice
# Alice 404-502, 894-005, 439-095
# Nick +16507811251
# Ben
# Alex +4(908)273-22-42
# Alice
# Nick
# Robert 51234047129, 92174043215
# Alex
# Robert
# Sample Output:
# 210-220
# 89001234050, +70504321009
# 210-220, 404-502, 894-005, 439-095
# +16507811251
# +4(908)273-22-42
# 51234047129, 92174043215
print("Задание 7")


def manage_contacts(inputs):
    contacts = {}
    for input_line in inputs:
        if ' ' in input_line:
            name, numbers = input_line.split(maxsplit=1)
            if name in contacts:
                contacts[name].extend(numbers.split(', '))
            else:
                contacts[name] = numbers.split(', ')
        else:
            name = input_line
            if name in contacts:
                yield ', '.join(contacts[name])
            else:
                yield "Не найдено"


contacts_input = [
    "Ben 89001234050, +70504321009", "Alice 210-220", "Alice",
    "Alice 404-502, 894-005, 439-095", "Nick +16507811251", "Ben",
    "Alex +4(908)273-22-42", "Alice", "Nick", "Robert 51234047129, 92174043215", "Alex", "Robert"
]
for output in manage_contacts(contacts_input):
    print(output)
print("_______________")

# 8.	Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
# Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы:
# на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата.
# На практике, все выборщики от штата голосуют в соответствии с результатами голосования внутри штата, то есть на заключительной стадии выборов
# в голосовании участвуют штаты, имеющие различное число голосов. В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и
# число голосов, отданных за него в одном из штатов. Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.
# Участников нужно выводить в алфавитном порядке.
print("Задание 8")
import collections


def count_votes(votes):
    candidates = collections.defaultdict(int)
    for vote in votes:
        candidate, count = vote.split()
        candidates[candidate] += int(count)
    return candidates


n = int(input())
votes = [input() for _ in range(n)]
candidates = count_votes(votes)

for candidate in sorted(candidates.keys()):
    print(f"{candidate} {candidates[candidate]}")

# Input:
# 5
# Biden 100
# Trump 200
# Biden 300
# Trump 400
# Sanders 500
print("_______________")
