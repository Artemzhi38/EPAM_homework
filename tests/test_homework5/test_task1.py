import datetime

from homeworks.homework5.task1 import Homework, Student, Teacher


def test_teacher_class_args():
    """Testing that arguments of teacher-class object
    are accessible with 'object.parameter'"""
    teacher = Teacher('Shadrin', 'Daniil')
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'


def test_student_class_args():
    """Testing that arguments of student-class object
    are accessible with 'object.parameter'"""
    student = Student('Petrov', 'Roman')
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_homework_class_args():
    """Testing that arguments of homework-class object
    are accessible with 'object.parameter'"""
    homework_deadline = datetime.timedelta(days=0.0)
    homework = Homework('homework text', homework_deadline)
    assert isinstance(homework.created, type(datetime.datetime.now()))
    assert homework.deadline == homework_deadline
    assert homework.text == 'homework text'


def test_homework_class_is_active_method():
    """Testing that method 'is_active' of homework-class
    object returns True when homework is not expired and
    returns False when homework is expired"""
    homework = Homework('homework text', datetime.timedelta(days=5.0))
    expired_homework = Homework('homework text', datetime.timedelta(days=0.0))
    assert homework.is_active()
    assert not expired_homework.is_active()


def test_student_class_do_homework_method(capsys):
    """Testing that method 'do_homework' of student-class
    object returns homework-class object when same object
    given as argument is not expired. When this object is
    expired it should print 'You are late' and return None"""
    student = Student('Petrov', 'Roman')
    homework = Homework('homework text', datetime.timedelta(days=5.0))
    expired_homework = Homework('homework text', datetime.timedelta(days=0.0))
    student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out.strip() == "You are late"
    assert student.do_homework(homework) == homework
    assert student.do_homework(expired_homework) is None


def test_teacher_class_create_homework_method():
    """Testing that method 'create_homework' of teacher-class
    object returns homework-class object with 'deadline' argument
    equal with 'days' argument of 'create_homework' method"""
    teacher = Teacher('Shadrin', 'Daniil')
    homework = teacher.create_homework('homework text', 5)
    assert homework.is_active()
    assert isinstance(homework, Homework)
    assert homework.deadline == datetime.timedelta(days=5.0)
