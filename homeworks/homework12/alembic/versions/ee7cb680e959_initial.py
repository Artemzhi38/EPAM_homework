"""Initial

Revision ID: ee7cb680e959
Revises:
Create Date: 2021-10-29 20:01:21.559585

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ee7cb680e959'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homeworks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.String(), nullable=True),
                    sa.Column('deadline', sa.Interval(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('teachers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('results',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('homework_id', sa.Integer(), nullable=True),
                    sa.Column('solution', sa.String(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['students.id'], ),
                    sa.ForeignKeyConstraint(['homework_id'],
                                            ['homeworks.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('teachers')
    op.drop_table('students')
    op.drop_table('homeworks')
    # ### end Alembic commands ###
