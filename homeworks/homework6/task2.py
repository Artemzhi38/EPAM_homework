"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Homework:
    """Атрибуты:
        text - текст задания
        deadline - хранит объект datetime.timedelta с количеством
        дней на выполнение
        created - c точной датой и временем создания
    Методы:
        is_active - проверяет не истекло ли время на выполнение задания,
        возвращает boolean
    """
    def __init__(self, text: str, deadline: datetime.timedelta,):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class Person:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """Атрибуты:
        last_name
        first_name
    Методы:
        do_homework - принимает объект Homework и возвращает его же, если
        задание уже просрочено, то печатет 'You are late' и возвращает None
    """
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        raise DeadlineError('You are late')


class DeadlineError(Exception):
    pass


class HomeworkResult:
    """Атрибуты:
        homework - для объекта Homework, если передан не этот класс -  выкинуть
        подходящие по смыслу исключение с сообщением:
        'You gave a not Homework object'
        solution - хранит решение ДЗ как строку
        author - хранит объект Student
        created - c точной датой и временем создания"""
    def __init__(self, homework, solution: str, author):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        else:
            self.homework = homework
            self.solution = solution
            self.author = author
            self.created = datetime.datetime.now()


class Teacher(Person):
    """Атрибуты:
        last_name
        first_name
        homework_done
    Методы:
        create_homework - текст задания и количество дней на это задание,
        возвращает экземпляр Homework. Обратите внимание, что для работы
        этого метода не требуется сам объект.
        check_homework - принимает экземпляр HomeworkResult и возвращает True
        если ответ студента больше 5 символов, так же при успешной проверке
        добавить в homework_done.
        Если меньше 5 символов - никуда не добавлять и вернуть False.
        reset_results - если передать экземпряр Homework - удаляет только
        результаты этого задания из homework_done, если ничего не передавать,
        то полностью обнулит homework_done."""
    homework_done = defaultdict(set)

    def check_homework(self, homework_result: HomeworkResult):
        if len(homework_result.solution) >= 5:
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if not homework:
            cls.homework_done = defaultdict(set)
        else:
            cls.homework_done[homework] = set()

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, datetime.timedelta(days=days))
