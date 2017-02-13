# -*- coding: utf-8 -*-
from __future__ import print_function

from postgres.api import is_valid_postgres_string
from django_productline.testingutils import NoMigrationsTestCase


class TestDBUsernameValidity(NoMigrationsTestCase):

    def test_is_valid_postgres_string_1(self):
        user_name = "Peter"
        self.assertTrue(is_valid_postgres_string(user_name))

    def test_is_valid_postgres_string_2(self):
        user_name = "peter"
        self.assertTrue(is_valid_postgres_string(user_name))

    def test_is_valid_postgres_string_3(self):
        user_name = "peter_mueller"
        self.assertTrue(is_valid_postgres_string(user_name))

    def test_is_valid_postgres_string_4(self):
        user_name = "Peter_Mueller"
        self.assertTrue(is_valid_postgres_string(user_name))

    def test_is_valid_postgres_string_5(self):
        user_name = "Peter_Mueller1"
        self.assertTrue(is_valid_postgres_string(user_name))

    def test_is_valid_postgres_string_6(self):
        user_name = "Peter_Müller"
        self.assertTrue(is_valid_postgres_string(user_name))

