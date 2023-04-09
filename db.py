import os

import my_web_app
from my_web_app.data.dbsession import DbSessionFactory


def includeme(config):
    top_folder = os.path.dirname(my_web_app.__file__)
    rel_folder = os.path.join('db', 'blue_yellow.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)
