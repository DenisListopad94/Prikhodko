# 1.	Создайте систему управления задачами с использованием классов. Реализуйте классы "Task", "Project" и "ProjectManager".
# Каждая задача должна содержать описание, статус (выполнена или нет) и срок выполнения.
# Проект должен включать в себя список задач и методы для добавления новой задачи, отметки задачи как выполненной и вывода списка всех задач.
print("Задание 1")


class Task:
    def __init__(self, description, status, deadline):
        self.description = description
        self.status = status
        self.deadline = deadline


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, task):
        task.status = "Done"

    def get_all_tasks(self):
        return self.tasks


class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_all_projects(self):
        return self.projects


project_manager = ProjectManager()

project = Project("My Project")

task1 = Task("Task 1", "Not Done", "2023-12-31")
task2 = Task("Task 2", "Done", "2023-11-30")

project.add_task(task1)
project.add_task(task2)

project_manager.add_project(project)

for task in project.get_all_tasks():
    print(task.description)
print("_______________")

# 2.	Создайте систему для управления бронированием билетов в авиакомпании. Реализуйте классы "Passenger", "Ticket", "Flight" и "Airline ".
# Каждый пассажир должен иметь атрибуты, такие как имя и фамилия. Билет должен содержать информацию о пассажире и маршруте полета.
# Рейс должен включать в себя список зарезервированных билетов. Авиакомпания должна иметь методы для бронирования билета, отмены брони и
# отображения списка зарезервированных билетов.
print("Задание 2")


class Passenger:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Ticket:
    def __init__(self, passenger, route):
        self.passenger = passenger
        self.route = route


class Flight:
    def __init__(self, flight_number, route):
        self.flight_number = flight_number
        self.route = route
        self.tickets = []

    def reserve_ticket(self, ticket):
        self.tickets.append(ticket)

    def cancel_ticket(self, ticket):
        self.tickets.remove(ticket)


class Airline:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_reserved_tickets(self):
        reserved_tickets = []
        for flight in self.flights:
            reserved_tickets += flight.tickets
        return reserved_tickets


passenger = Passenger("Иван", "Иванов")

ticket = Ticket(passenger, "Минск - Москва")

flight = Flight("SU-123", "Минск - Москва")

flight.reserve_ticket(ticket)
print("_______________")

# 3.	Создать абстрактный класс «Alive». Определить наследуемые классы – «Fox», «Rabbit» и «Plant». Лисы едят кроликов. Кролики едят растения.
# Растение поглощают солнечный свет. Представители каждого класса могут умереть, если достигнут определенного возраста или для них не будет еды.
# Напишите виртуальные методы поедания и определения состояния живых существа (живые или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
print("Задание 3")

# В этом коде класс Alive является абстрактным базовым классом, который определяет общие свойства и методы для всех живых существ.
# Классы Fox, Rabbit и Plant наследуются от класса Alive и реализуют свои собственные методы eat() и is_alive().
# Метод eat() определяет, что живое существо ест, а метод is_alive() определяет, живо ли оно в зависимости от возраста и наличия еды.
# В классе Fox метод eat() определяет, что лисы едят кроликов, а метод is_alive() определяет, что лиса умирает, если ей больше 5 лет или у нее нет еды.
# В классе Rabbit метод eat() определяет, что кролики едят растения, а метод is_alive() определяет, что кролик умирает, если ему больше 3 лет или у него нет еды.
# В классе Plant метод eat() определяет, что растение поглощает солнечный свет, а метод is_alive() определяет, что растение умирает, если ему больше 10 лет.
from abc import ABC, abstractmethod


class Alive(ABC):
    def __init__(self, age, food):
        self.age = age
        self.food = food

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass


class Fox(Alive):
    def __init__(self, age, food):
        super().__init__(age, food)

    def eat(self, rabbit):
        if isinstance(rabbit, Rabbit):
            self.food += 1
            rabbit.food -= 1
            return True
        return False

    def is_alive(self):
        if self.age > 5 or self.food < 1:
            return False
        return True


class Rabbit(Alive):
    def __init__(self, age, food):
        super().__init__(age, food)

    def eat(self, plant):
        if isinstance(plant, Plant):
            self.food += 1
            plant.food -= 1
            return True
        return False

    def is_alive(self):
        if self.age > 3 or self.food < 1:
            return False
        return True


class Plant(Alive):
    def __init__(self, age, food):
        super().__init__(age, food)

    def eat(self):
        self.food += 1

    def is_alive(self):
        if self.age > 10:
            return False
        return True


fox = Fox(3, 2)

rabbit = Rabbit(1, 5)
fox.eat(rabbit)

print(fox.is_alive())

print(fox.food)
print("_______________")
