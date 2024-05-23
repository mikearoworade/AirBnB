#!/usr/bin/python3
"""Defines unittests for models/base_model.py

Unittest classes:
    TestBaseModel_instantation
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing the instantiation of the BaseModel Class"""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    

if __name__ == "__main__":
    unittest.main()
