"""Using ORM framework of your choice, create models classes created in
Homework 6 (Teachers, Students, Homework and others). - Target database
 should be sqlite (filename main.db localted in current directory) - ORM
 framework should support migrations.

Utilizing that framework capabilities, create
- a migration file, creating all necessary database structures.
- a migration file (separate) creating at least one record in each created
  database table

(*) optional task: write standalone script (get_report.py) that retrieves
and stores the following information into CSV file report.csv
for all done (completed) homeworks:
    Student name (who completed homework) Creation date Teacher name who
    created homework
Utilize ORM capabilities as much as possible, avoiding executing raw SQL
queries."""

import datetime
from collections import defaultdict
from sqlalchemy import Column, Integer, String, Interval, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Person:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class DeadlineError(Exception):
    pass


engine = create_engine('sqlite:///main.db', echo=True)

Base = declarative_base()


class HomeworkResult(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homeworks.id'))
    solution = Column(String)
    author_id = Column(Integer, ForeignKey('students.id'))
    hr_hw = relationship("Homework", back_populates="hw")
    hr_st = relationship("Student", back_populates="st")

    def __init__(self, homework, solution: str, author):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        else:
            self.homework = homework
            self.solution = solution
            self.author = author
            self.created = datetime.datetime.now()
            self.homework_id = homework.id
            self.author_id = author.id


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(Interval)
    hw = relationship("HomeworkResult", back_populates="hr_hw")

    def __init__(self, text: str, deadline: datetime.timedelta,):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class Student(Person, Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    st = relationship("HomeworkResult", back_populates="hr_st")

    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        raise DeadlineError('You are late')


class Teacher(Person, Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)

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


# Создание таблицы
Base.metadata.create_all(engine)
