import sys
import unittest
from model.secretData import SecretData
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock
from db.createSecret import createSecret
from manageSecret.manageSecret import createSecretDAO
class ManageSecret_test(unittest.TestCase):
    def test_create_secret_without_text(self):
        foo = SecretData("", 5, datetime.now())
        with self.assertRaises(Exception):
            createSecretDAO(foo)
    def test_create_secret_without_zero_visits(self):
        foo = SecretData("foo", 0, datetime.now())
        with self.assertRaises(Exception):
            createSecretDAO(foo)
    def test_create_secret_without_exp_date(self):
        foo = SecretData("foo", 5, None)
        with self.assertRaises(Exception):
            createSecretDAO(foo)
    def test_create_secret_with_no_data(self):
        foo = SecretData("", 0, None)
        with self.assertRaises(Exception):
            createSecretDAO(foo)
    @patch(target="manageSecret.manageSecret.createSecret")
    def test_creating_data(self, mock_createSecret : Mock):
        foo = SecretData("foo", 5, datetime.now())
        createSecretDAO(foo)
        mock_createSecret.assert_called_once()
        
