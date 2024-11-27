#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2015 John Törnblom

import logging

from setuptools import setup

logging.basicConfig(level=logging.DEBUG)

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
        'Programming Language :: Python :: 3 :: Only'],
    keywords='rsl xtuml bridgepoint',
    packages=['rsl', 'examples'],
    data_files = [('share/gtksourceview-3.0/language-specs',
                    ['editors/gtksourceview/rsl.lang'])],
    requires=['ply', 'pyxtuml'],
    install_requires=['ply', 'pyxtuml'],
    setup_requires=['ply', 'pyxtuml'])

# assure PLY parstab and lextab get generated
import rsl
rsl.parse_text('')
