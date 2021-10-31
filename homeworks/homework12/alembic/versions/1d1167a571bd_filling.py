"""filling

Revision ID: 1d1167a571bd
Revises: ee7cb680e959
Create Date: 2021-10-30 13:34:02.101359

"""
import datetime

from alembic import op
from sqlalchemy import Integer, Interval, String
from sqlalchemy.sql import column, table

# revision identifiers, used by Alembic.
revision = '1d1167a571bd'
down_revision = 'ee7cb680e959'
branch_labels = None
depends_on = None


def upgrade():
    teachers = table('teachers',
                     column('last_name', String),
                     column('first_name', String)
                     )
    op.bulk_insert(teachers, [{'last_name': 'Shadrin',
                               'first_name': 'Daniil'}, ])
    students = table('students',
                     column('last_name', String),
                     column('first_name', String)
                     )
    op.bulk_insert(students, [{'last_name': 'Petrov',
                               'first_name': 'Roman'}, ])
    homeworks = table('homeworks',
                      column('text', String),
                      column('deadline', Interval)
                      )
    op.bulk_insert(homeworks, [{'text': 'homework text',
                                'deadline': datetime.timedelta(days=2.0)}, ])
    results = table('results',
                    column('homework_id', Integer),
                    column('solution', String),
                    column('author_id', Integer)
                    )
    op.bulk_insert(results, [{'homework_id': 1,
                              'solution': 'I have done this hw',
                              'author_id': 1}, ])


def downgrade():
    op.execute("delete from teachers")
    op.execute("delete from students")
    op.execute("delete from homeworks")
    op.execute("delete from results")
