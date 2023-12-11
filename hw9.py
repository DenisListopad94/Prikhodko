# 1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
# Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение из этих двух переменных.
print("Задание 1")


class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print_vars(self):
        print(f"var1: {self.var1}, var2: {self.var2}")

    def change_vars(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def sum_vars(self):
        return self.var1 + self.var2

    def max_var(self):
        return max(self.var1, self.var2)


my_class = MyClass(3, 5)
my_class.print_vars()
my_class.change_vars(4, 6)
my_class.print_vars()
print(f"Sum of vars: {my_class.sum_vars()}")
print(f"Max var: {my_class.max_var()}")
print("_______________")

# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне.
# Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. Написать программу,
# демонстрирующую все возможности класса.
print("Задание 2")


class DecimalCounter:
    def __init__(self, min_value=0, max_value=10, initial_value=0):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = initial_value

    def increase(self):
        if self.current_value < self.max_value:
            self.current_value += 1

    def decrease(self):
        if self.current_value > self.min_value:
            self.current_value -= 1

    @property
    def current_state(self):
        return self.current_value


counter = DecimalCounter(min_value=0, max_value=10, initial_value=5)
print(counter.current_state)
counter.increase()
print(counter.current_state)
counter.decrease()
print(counter.current_state)
print("_______________")

# 3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, поиска продуктов по названию,
# добавления их в магазин и удаления продуктов из него.
print("Задание 3")


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity

    def remove_product(self, name, quantity):
        if name in self.products:
            if self.products[name] >= quantity:
                self.products[name] -= quantity
                if self.products[name] == 0:
                    del self.products[name]
            else:
                print("Error: Not enough quantity of product to remove.")
        else:
            print("Error: Product not found.")

    def search_product(self, name):
        if name in self.products:
            return self.products[name]
        else:
            return 0


my_shop = Shop()

my_shop.add_product("Яблоки", 10)
my_shop.add_product("Груши", 5)
my_shop.add_product("Бананы", 20)

print(my_shop.search_product("Яблоки"))
print(my_shop.search_product("Апельсины"))

my_shop.remove_product("Яблоки", 5)
my_shop.remove_product("Груши", 10)

print(my_shop.search_product("Яблоки"))
print(my_shop.search_product("Груши"))
print("_______________")

# 4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
# которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
# Класс должен иметь следующий вид:
#
# class MoneyBox:
#     def__init__(self, capacity) :
#     #конструктор с аргументом- вместимость копилки
#     def can_add(self,v)
#     #True, если можно добавить v монет, False иначе
#     def add(self,v)
#     #положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
print("Задание 4")


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v


box = MoneyBox(10)
print(box.can_add(5))
print(box.can_add(10))
print(box.can_add(11))
box.add(5)
print(box.can_add(6))
print("_______________")

# 1.	Задача на взаимодействие между классами. Разработать систему «Интернет-магазин».
# Товаровед добавляет информацию о Товаре. Клиент делает заявку на товар, если товар есть в наличие в магазине
# то покупатель оплачивает товар иначе товаровед делает запрос на склад о наличии товара.
print("Доп задание 1")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_product(self, product):
        if product in self.products:
            return True
        else:
            return False


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def place_order(self, product, store):
        if store.check_product(product):
            print("Your order has been placed.")
        else:
            print("Sorry, the product is not available.")


class Clerk:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def request_product(self, product, store):
        if not store.check_product(product):
            print("Requesting product from warehouse...")
            # Code to request product from warehouse goes here
            store.add_product(product)
            print("Product added to store.")
        else:
            print("Product is already in store.")


product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)

store = Store()
store.add_product(product1)
store.add_product(product2)

customer = Customer("John", "john@example.com")
clerk = Clerk("Mary", "mary@example.com")

customer.place_order(product1, store)
clerk.request_product(product2, store)

print("_______________")
