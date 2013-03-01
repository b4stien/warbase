 # -*- coding: utf-8 -*-
import unittest

from warbase.model import User, Action, ComputedValue

from . import TestData


class TestModelBase(TestData):

    def test_user(self):
        user = User.User()
        self.assertTrue(True)

    def test_action(self):
        user = Action.Action()
        self.assertTrue(True)

    def test_computed_value(self):
        user = ComputedValue.ComputedValue()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
