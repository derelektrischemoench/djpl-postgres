# -*- coding: utf-8 -*-
from __future__ import print_function

from postgres.api import is_valid_postgres_string
from django_productline.testingutils import NoMigrationsTestCase


class TestDBNameValidity(NoMigrationsTestCase):

    def test_is_valid_postgres_string_1(self):
        database_name = "test"
        self.assertTrue(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_2(self):
        database_name = "test1"
        self.assertTrue(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_3(self):
        database_name = "test_1"
        self.assertTrue(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_4(self):
        database_name = "test 1"
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_5(self):
        database_name = "Test1"
        self.assertTrue(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_6(self):
        database_name = "Täst_1"
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_7(self):
        database_name = "TEST"
        self.assertTrue(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_8(self):
        database_name = "test-1"
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_9(self):
        database_name = " "
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_10(self):
        database_name = "dies.das"
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_11(self):
        database_name = "!!!!"
        self.assertFalse(is_valid_postgres_string(database_name))

    def test_is_valid_postgres_string_12(self):
        database_name = "øłæ→ŋħđø→ħ€łđøłæ→↓ħđæðħđ"
        self.assertFalse(is_valid_postgres_string(database_name))
