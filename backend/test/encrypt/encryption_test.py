import pytest
from encrypt.encryption import encryptSecret, decryptSecret 
from base64 import b64encode, b64decode
from db.visitSecret import getSecretFromDb
from unittest.mock import patch, Mock


class Test_Encryption():

    # EncryptSecret tests
    def test_encrypt_secret(self):
        foo = "secret"
        expected = b64encode(foo.encode("ascii")).decode("ascii")
        actual = encryptSecret(foo)
        assert expected == actual
    #decryptSecret tests
    @patch(target="db.visitSecret.getSecretFromDb")
    def test_decrypt_with_empty_string(self, mock_getSecret : Mock):
        mock_getSecret.return_value = ""
        expected = ""
        actual = decryptSecret("foo")
        assert expected == actual
    @patch(target="db.visitSecret.getSecretFromDb")
    def test_decrypt_with_none(self, mock_getSecret : Mock):
        mock_getSecret.return_value = None
        expected = ""
        actual = decryptSecret("foo")
        assert expected == actual
    @patch(target="db.visitSecret.getSecretFromDb")
    def test_decrypt_with_number(self, mock_getSecret : Mock):
        mock_getSecret.return_value = 5
        expected = ""
        actual = decryptSecret("foo")
        assert expected == actual
