#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2015 John Törnblom

import logging
import unittest
import os
import sys
import stat
import zipfile

from setuptools import setup
from setuptools import Command
from setuptools.command.build_py import build_py


logger = logging.getLogger('setup')
logging.basicConfig(level=logging.DEBUG)


class BuildCommand(build_py):
    
    def run(self):
        import rsl

        rsl.parse_text('', '')
        build_py.run(self)


class TestCommand(Command):
    description = "Execute unit tests"
    user_options = [('name=', None, 'Limit testing to a single test case or test method')]

    def initialize_options(self):
        self.name = None
    
    def finalize_options(self):
        if self.name and not self.name.startswith('tests.'):
            self.name = 'tests.' + self.name

    def run(self):
        if self.name:
            suite = unittest.TestLoader().loadTestsFromName(self.name)
        else:
            suite = unittest.TestLoader().discover('tests')
        
        runner = unittest.TextTestRunner(verbosity=2, buffer=True)
        exit_code = not runner.run(suite).wasSuccessful()
        sys.exit(exit_code)


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()

setup(name='pyrsl',
    version='3.0.0', # ensure that this is the same as in rsl.version
    description='Interpreter for the Rule Specification Language (RSL)',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='John Törnblom',
    author_email='john.tornblom@gmail.com',
    url='https://github.com/xtuml/pyrsl',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
    keywords='rsl xtuml bridgepoint',
    packages=['rsl'],
    data_files = [('share/gtksourceview-3.0/language-specs',
                    ['editors/gtksourceview/rsl.lang'])],
    requires=['ply', 'xtuml'],
    setup_requires=['ply', 'pyxtuml'],
    cmdclass={'build_py': BuildCommand,
                'test': TestCommand})
