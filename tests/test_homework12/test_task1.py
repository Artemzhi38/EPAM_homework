import datetime
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homeworks.homework12.alembic.task1_db_creation import (Homework,
                                                            HomeworkResult,
                                                            Student, Teacher)


@pytest.fixture
def db_session_fixture():
    path_to_db = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
        os.path.dirname(__file__)))), 'homeworks', 'homework12', 'main.db')
    engine = create_engine('sqlite:///'+path_to_db, echo=False)
    session_class = sessionmaker(bind=engine)
    session = session_class()
    yield session
    session.close()


def test_add_some_records(db_session_fixture):
    session = db_session_fixture

    # DB commit
    web_teacher = Teacher('Ivanov', 'Ivan')
    session.add(web_teacher)
    good_student = Student('Petrov', 'Petr')
    session.add(good_student)
    web_homework = Homework('do web homework', datetime.timedelta(days=5.0))
    session.add(web_homework)
    session.flush()
    good_student_web_result = HomeworkResult(
        web_homework, 'Web homework done!', good_student)
    session.add(good_student_web_result)
    session.commit()

    # checking comitted changes
    res = session.query(Teacher).order_by(Teacher.id)
    assert res[1].id == 2
    assert res[1].last_name == 'Ivanov'
    assert res[1].first_name == 'Ivan'
    res = session.query(Student).order_by(Student.id)
    assert res[1].id == 2
    assert res[1].last_name == 'Petrov'
    assert res[1].first_name == 'Petr'
    res = session.query(Homework).order_by(Homework.id)
    assert res[1].id == 2
    assert res[1].text == 'do web homework'
    assert res[1].deadline == datetime.timedelta(days=5.0)
    res = session.query(HomeworkResult).order_by(HomeworkResult.id)
    assert res[1].id == 2
    assert res[1].homework_id == 2
    assert res[1].solution == 'Web homework done!'
    assert res[1].author_id == 2
    session.delete(web_teacher)
    session.delete(web_homework)
    session.delete(good_student)
    session.delete(good_student_web_result)
    session.commit()


def test_read_default_rows(db_session_fixture):
    session = db_session_fixture
    res = session.query(Teacher).order_by(Teacher.id)
    assert res[0].id == 1
    assert res[0].last_name == 'Shadrin'
    assert res[0].first_name == 'Daniil'
    res = session.query(Student).order_by(Student.id)
    assert res[0].id == 1
    assert res[0].last_name == 'Petrov'
    assert res[0].first_name == 'Roman'
    res = session.query(Homework).order_by(Homework.id)
    assert res[0].id == 1
    assert res[0].text == 'homework text'
    assert res[0].deadline == datetime.timedelta(days=2.0)
    res = session.query(HomeworkResult).order_by(HomeworkResult.id)
    assert res[0].id == 1
    assert res[0].homework_id == 1
    assert res[0].solution == 'I have done this hw'
    assert res[0].author_id == 1
