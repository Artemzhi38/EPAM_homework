import datetime

from collections import defaultdict

import pytest
from homeworks.homework6.task2 import (DeadlineError, Homework, HomeworkResult,
                                       Student, Teacher)


def test_homework_result_class_args():
    """Testing that arguments of HomeworkResult-class object
    are accessible with 'object.parameter'"""
    average_student = Student('Petrov', 'Roman')
    oop_homework = Homework('homework text', datetime.timedelta(days=0.0))
    average_students_oop_homework_result = \
        HomeworkResult(oop_homework, 'some solution', average_student)
    assert average_students_oop_homework_result.homework == oop_homework
    assert average_students_oop_homework_result.solution == 'some solution'
    assert average_students_oop_homework_result.author == average_student


def test_not_a_homework_class_object_given_to_homework_result():
    """Testing that in case of receiving not a
    Homework-class object as a first argument
    in HomeworkResult object interpreter will
    rise TypeError with 'You gave a not Homework
    object' message"""
    average_student = Student('Petrov', 'Roman')
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult('not a Homework-class object',
                       'some solution', average_student)


def test_do_homework_method_returns_homework_result_object():
    """Testing that in case of non-expired-homework arg,
    output of do_homework method of Student class is
    HomeworkResult-class object"""
    average_student = Student('Petrov', 'Roman')
    non_expired_homework = Homework('homework text',
                                    datetime.timedelta(days=5.0))
    result = average_student.do_homework(non_expired_homework, 'some solution')
    assert isinstance(result, HomeworkResult)


def test_do_homework_method_raises_deadline_error():
    """Testing that in case of expired-homework arg,
    do_homework method of Student class will raise
    DeadlineError with 'You are late' message"""
    average_student = Student('Petrov', 'Roman')
    expired_homework = Homework('homework text', datetime.timedelta(days=0.0))
    with pytest.raises(DeadlineError, match="You are late"):
        average_student.do_homework(expired_homework, 'some solution')


def test_homework_done_attr_of_teacher_class():
    """Testing that homework_done attr of Teacher class is
    joint for all objects of Teacher class instance of
    defaultdict collection and it's values are instances
    of set class"""
    oop_teacher = Teacher('Shadrin', 'Daniil')
    testing_teacher = Teacher('Volkov', 'Anton')
    assert isinstance(oop_teacher.homework_done, defaultdict)
    assert isinstance(Teacher.homework_done['oop_homework'], set)
    assert oop_teacher.homework_done == testing_teacher.homework_done


def test_check_homework_method_of_teacher_class():
    """Testing that check_homework method of Teacher class:
    - returns True when given HomeworkResult-object with
      solution arg that is not less than 5 chars and adds this
       object to homework_done attr
    - returns False when given HomeworkResult-object with
      solution arg less than 5 chars and doesn't add this object
      to homework_done attr"""
    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')
    oop_teacher = Teacher('Shadrin', 'Daniil')
    oop_hw = oop_teacher.create_homework('Learn OOP', 1)
    docs_hw = oop_teacher.create_homework('Read docs', 5)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    assert oop_teacher.check_homework(result_1)
    assert oop_teacher.check_homework(result_2)
    assert not oop_teacher.check_homework(result_3)
    assert result_1 in Teacher.homework_done[oop_hw]
    assert result_2 in Teacher.homework_done[docs_hw]
    assert result_3 not in Teacher.homework_done[oop_hw]


def test_reset_results_method_of_teacher_class():
    """Testing that reset_results method of Teacher class:
    - deletes all HomeworkResult-objects from corresponding
      set in homework_done when given Homework-object as an
      argument
    - deletes all HomeworkResult-objects from all sets
      in homework_done when not given any argument"""
    good_student = Student('Lev', 'Sokolov')
    oop_teacher = Teacher('Shadrin', 'Daniil')
    oop_hw = oop_teacher.create_homework('Learn OOP', 1)
    docs_hw = oop_teacher.create_homework('Read docs', 5)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    oop_teacher.check_homework(result_1)
    oop_teacher.check_homework(result_2)
    assert result_1 in Teacher.homework_done[oop_hw]
    assert result_2 in Teacher.homework_done[docs_hw]
    Teacher.reset_results(oop_hw)
    assert result_1 not in Teacher.homework_done[oop_hw]
    assert result_2 in Teacher.homework_done[docs_hw]
    Teacher.reset_results()
    assert result_1 not in Teacher.homework_done[oop_hw]
    assert result_2 not in Teacher.homework_done[docs_hw]
