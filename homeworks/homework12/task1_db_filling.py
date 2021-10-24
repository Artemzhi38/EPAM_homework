import datetime
from task1_db_creation import Teacher, Student, Homework, HomeworkResult
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///main.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

oop_teacher = Teacher('Shadrin', 'Daniil')
session.add(oop_teacher)
average_student = Student('Petrov', 'Roman')
session.add(average_student)
oop_homework = Homework('homework text', datetime.timedelta(days=2.0))
session.add(oop_homework)
session.commit()
average_student_oop_result = HomeworkResult(oop_homework, 'I have done this hw', average_student)
session.add(average_student_oop_result)
session.commit()


res = session.query(Teacher).order_by(Teacher.id)
for row in res:
    print(row.id, row.last_name, row.first_name)
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
