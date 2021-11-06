# encoding: utf-8
# Copyright (C) 2015 John Törnblom

import sys
import pytest

from utils import RSLTestCase
from utils import evaluate_docstring


class TestPrint(RSLTestCase):

    @evaluate_docstring
    def test_print_string(self, rc):
        '''
        .print "Hello world!"
        '''
        try:
            output = sys.stdout.getvalue().strip()
        except AttributeError:
            s, _ = self.capfd.readouterr()
            output = s.strip()
        self.assertEqual(output, "test_print.test_print_string: 2:  INFO:  Hello world!")
        
    @evaluate_docstring
    def test_print_substitution_variable(self, rc):
        '''
        .assign s = "world"
        .print "Hello ${s}!"
        '''
        try:
            output = sys.stdout.getvalue().strip()
        except AttributeError:
            s, _ = self.capfd.readouterr()
            output = s.strip()
        self.assertEqual(output, "test_print.test_print_substitution_variable: 3:  INFO:  Hello world!")
        
    @evaluate_docstring
    def test_print_double_dollar(self, rc):
        '''
        .assign s = "$$world"
        .print "Hello ${s}!"
        '''
        try:
            output = sys.stdout.getvalue().strip()
        except AttributeError:
            s, _ = self.capfd.readouterr()
            output = s.strip()
        self.assertEqual(output, "test_print.test_print_double_dollar: 3:  INFO:  Hello $world!")

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
