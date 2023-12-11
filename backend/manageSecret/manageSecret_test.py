from model.secretData import SecretData
from datetime import datetime
import pytest
from db import createSecret
from manageSecret.manageSecret import createSecretDAO
from unittest.mock import patch, Mock

class TestManageSecret():
    def test_create_secret_without_text(self):
        foo = SecretData("", 5, datetime.now())
        with pytest.raises(Exception):
            createSecretDAO(foo)
    def test_create_secret_without_zero_visits(self):
        foo = SecretData("foo", 0, datetime.now())
        with pytest.raises(Exception):
            createSecretDAO(foo)
    def test_create_secret_without_exp_date(self):
        foo = SecretData("foo", 5, None)
        with pytest.raises(Exception):
            createSecretDAO(foo)
    def test_create_secret_with_no_data(self):
        foo = SecretData("", 0, None)
        with pytest.raises(Exception):
            createSecretDAO(foo)
    @patch(target="manageSecret.manageSecret.createSecret")
    def test_creating_data(self, mock_createSecret : Mock):
        foo = SecretData("foo", 5, datetime.now())
        createSecretDAO(foo)
        mock_createSecret.assert_called_once()
        
