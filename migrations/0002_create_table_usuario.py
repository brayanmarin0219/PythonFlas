"""
create table usuario
date created: 2021-10-22 04:09:03.111111
"""


def upgrade(migrator):
    with migrator.create_table('usuario') as table:
        table.text('username')
        table.text('nombre')
        table.text('email')
        table.text('password')
        table.int('rol')


def downgrade(migrator):
    migrator.drop_table('usuario')
