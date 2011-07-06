# -*- coding: utf-8 -*-
"""pavement.py -- paver tasks for Project Euler problems.
"""
from paver.easy import *

@task
def test():
    sh('nosetests --all-modules')

