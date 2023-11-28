import sys
import unittest
from model.secretData import SecretData
from datetime import datetime
from manageSecret.manageSecret import createSecretDAO
class ManageSecret_test(unittest.TestCase):
    def test_create_secret_without_text(self):
        foo = SecretData("", 5, datetime.now())
        with self.assertRaises(Exception):
            createSecretDAO(foo)

print(sys.path)