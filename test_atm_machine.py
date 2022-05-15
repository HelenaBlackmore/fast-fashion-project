import unittest
import sys
from unittest import TestCase, main
from unittest import mock

from ATM_MACHINE import withdraw

class TestWithdraw(unittest.TestCase):
    def test_function(self):
        sys.stdin = open("preprogrammed_inputs.txt")
        module.call_function()

    def setup_method(self):
        self.orig_stdin = sys.stdin

    def teardown_method(self):
        sys.stdin = self.orig_stdin