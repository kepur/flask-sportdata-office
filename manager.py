"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app.models import *
from app import sport_index

magrate = Migrate(sport_index,db)
manager=Manager(sport_index)
manager.add_command('db',MigrateCommand)

@manager.command
def init_databases():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()