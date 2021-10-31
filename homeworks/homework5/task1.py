"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework
2. Student
3. Teacher

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


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


class Student:
    """Атрибуты:
        last_name
        first_name
    Методы:
        do_homework - принимает объект Homework и возвращает его же, если
        задание уже просрочено, то печатет 'You are late' и возвращает None
    """
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(hw: Homework):
        if hw.is_active():
            return hw
        print('You are late')


class Teacher:
    """Атрибуты:
        last_name
        first_name
    Методы:
        create_homework - текст задания и количество дней на это задание,
        возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект."""
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, datetime.timedelta(days=days))


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    print(teacher.last_name)  # Daniil
    print(student.first_name)  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    print(type(student.do_homework(oop_homework)))
    print(student.do_homework(expired_homework))  # You are late
