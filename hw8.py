# 1.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак.
print("Задание 1")

with open("first_task.txt", "r", encoding="utf-8") as file:
    result = '\n'.join(map(lambda x: f"{x}!", file.read().split('\n')))
print(result)
print("_______________")

# 2.	Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа.
# Затем записать их произведение в файл output.txt.
print("Задание 2")
with open("input.txt", "w") as file:
    file.write("1 2 3 4 5 6 7 8 9 10")
with open("input.txt", "r") as file:
    numbers = file.read().split()
numbers = [int(number) for number in numbers]
product = 1
for number in numbers:
    product *= number

with open("output.txt", "w") as file:
    file.write(str(product))
print("_______________")

# 3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
# цену единицы и дату поступления товара на склад. Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р.
print("Задание 3")
from datetime import datetime, timedelta

goods = [
    {'name': 'Товар 1', 'quantity': 10, 'price': 1000000, 'date': datetime(2023, 11, 1)},
    {'name': 'Товар 2', 'quantity': 5, 'price': 500000, 'date': datetime(2023, 10, 2)},
    {'name': 'Товар 3', 'quantity': 20, 'price': 2000000, 'date': datetime(2023, 9, 3)},
    {'name': 'Товар 4', 'quantity': 15, 'price': 1500000, 'date': datetime(2023, 8, 4)},
    {'name': 'Товар 5', 'quantity': 25, 'price': 2500000, 'date': datetime(2023, 7, 5)}
]

with open('goods.txt', 'w', encoding="utf-8") as f:
    for good in goods:
        f.write(f"{good['name']}, {good['quantity']}, {good['price']}, {good['date']}\n")

today = datetime.now()
for good in goods:
    if good['date'] < today - timedelta(days=30) and good['price'] > 1000000:
        print(f"{good['name']} - {good['quantity']} ед., стоимость {good['price']} руб.")
print("_______________")
# Тут не совсем поняла что нужно было сделать в задаче с файлом, поэтому создала файл из списка товаров.

# 4.	Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий из 2-ух элементов –
# имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
print("Задание 4")
import json

my_dict = {
    12345: ("Marina", 28),
    23456: ("Darya", 28),
    34567: ("David", 30),
    45678: ("Yana", 33),
    56789: ("Ann", 32)
}

with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)
print("_______________")

# 5.	Прочитать сохранённый json – файл и записать данные на диск в csv файл.
# Первое значение каждой строки должно начинаться со слова person, значения разделить ;
print("Задание 5")
import json
import csv


def convert_json_to_csv(json_file_path, csv_file_path):
    """
    Функция, которая конвертирует json файл в csv, добавляя к первому значению каждой строки "person" и разделяя значения ;
    Args:
        json_file_path: json-файл в директории проекта
        csv_file_path: csv-файл в директории проекта
    Returns: csv-файл с данными из json-файла
    """
    # Чтение данных из JSON файла
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    # Запись данных в CSV файл
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        # Запись данных
        for key, value in data.items():
            row = [f'person {key}, {value[0]}, {value[1]}', '']
            csv_writer.writerow(row)


json_file_path = 'my_dict.json'  # Предполагаемый путь к JSON файлу
csv_file_path = 'task5.csv'     # Путь для сохранения CSV файла
convert_json_to_csv(json_file_path, csv_file_path)
print("_______________")

# 6.	Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
# x = (1, 2, 5, 7)
# x = x  / 2
# print(x)
print("Задание 6")
try:
    x = (1, 2, 5, 7)
    x = x / 2
except TypeError as e:
    print(f"Тип ошибки: {type(e).__name__}. Комментарий: {e}")
print("_______________")

# 7.	Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
print("Задание 7")
my_list = [1, 2, 3]
try:
    print(my_list[3])
except IndexError:
    print("Вы пытаетесь взять индекс элемента, которого нет в списке")
print("_______________")

# 8.	Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.
print("Задание 8")
try:
    string = "Hello"
    number = 123
    result = string + number
except TypeError:
    print("Вы пытаетесь сложить строку и число")
print("_______________")

# 9.	Напишите программу которые будет ловить FileNotFoundError, когда вы пытаетесь открыть файл для чтения, которого не существует.
print("Задание 9")
try:
    with open('несуществующий_файл.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')
print("_______________")

# 10.	Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
# когда пользователь пытается удалить элемент которого нет в списке.
print("Задание 10")
my_list = [1, 2, 3, 4, 5]
try:
    my_list.remove(6)
except ValueError:
    raise TypeError("The element you are trying to remove is not in the list.")
print("_______________")

# 11.	Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово
# в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое.
# Для решение вам необходимо открыть файл для чтения 11.txt .
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3
print("Доп задание 11")
with open('11.txt', 'r') as f:
    text = f.read().lower().split()

word_count = {}
for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_word = ''
max_count = 0
for word, count in word_count.items():
    if count > max_count or (count == max_count and word < max_word):
        max_word = word
        max_count = count

print(max_word, max_count)
print("_______________")
