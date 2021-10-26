import datetime
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1_db_creation import Homework, HomeworkResult, Student, Teacher

path_to_db = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'main.db')
engine = create_engine('sqlite:///'+path_to_db, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# First commit
oop_teacher = Teacher('Shadrin', 'Daniil')
session.add(oop_teacher)
average_student = Student('Petrov', 'Roman')
session.add(average_student)
oop_homework = Homework('homework text', datetime.timedelta(days=2.0))
session.add(oop_homework)
session.flush()
# Second commit
average_student_oop_result = HomeworkResult(
    oop_homework, 'I have done this hw', average_student)
session.add(average_student_oop_result)
session.commit()
session.rollback()
# Show all tables contents
res = session.query(Teacher).order_by(Teacher.id)
print(res[1].id)
print(res[1].last_name)
print(res[1].first_name)
print()
res = session.query(Student).order_by(Student.id)
for row in res:
    print(row.id, row.last_name, row.first_name)
print()
res = session.query(Homework).order_by(Homework.id)
for row in res:
    print(row.id, row.text, row.deadline)
print()
res = session.query(HomeworkResult).order_by(HomeworkResult.id)
for row in res:
    print(row.id, row.homework_id, row.solution, row.author_id)
