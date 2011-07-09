# -*- coding: utf-8 -*-
"""pavement.py -- paver tasks for Project Euler problems.
"""
from paver.easy import *
from paved.util import shv

__path__ = path(__file__).abspath().dirname()


@task
def test():
    shv('nosetests --all-modules')

@task
@consume_args
def run(args):
    for fn in __path__.listdir('e*.py'):
        for arg in args:
            if fn.namebase.endswith(arg):
                print '\n\n---------------->'
                shv('time python %s' % fn)
