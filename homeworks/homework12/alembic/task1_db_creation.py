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
import os

from sqlalchemy import (Column, ForeignKey, Integer, Interval, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

path_to_db = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'main.db')
engine = create_engine('sqlite:///'+path_to_db, echo=True)
Base = declarative_base()


class HomeworkResult(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homeworks.id'))
    solution = Column(String)
    author_id = Column(Integer, ForeignKey('students.id'))
    hr_hw = relationship("Homework", back_populates="hw")
    hr_st = relationship("Student", back_populates="st")


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(Interval)
    hw = relationship("HomeworkResult", back_populates="hr_hw")


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    st = relationship("HomeworkResult", back_populates="hr_st")


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
