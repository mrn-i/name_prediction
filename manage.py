#!/usr/bin/env python3

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from name_predict_app.views import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()

