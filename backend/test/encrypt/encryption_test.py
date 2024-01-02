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
    #The input params are redundant, because I don't test the db queries here.
    @patch(target="encrypt.encryption.db.getSecretFromDb")
    def test_decrypt_with_empty_string(self, mock_getSecretFromDb : Mock):
        mock_getSecretFromDb.return_value = ""
        expected = ""
        actual = decryptSecret("foo")
        assert expected == actual
        mock_getSecretFromDb.assert_called_once()
    @patch(target="encrypt.encryption.db.getSecretFromDb")
    def test_decrypt_with_none(self, mock_getSecret : Mock):
        mock_getSecret.return_value = None
        expected = ""
        actual = decryptSecret("foo")
        assert expected == actual
        mock_getSecret.assert_called_once()
    @patch(target="encrypt.encryption.db.getSecretFromDb")
    def test_decrypt_with_number(self, mock_getSecret : Mock):
        mock_getSecret.return_value = 5
        with pytest.raises(Exception) as exc_info:
            decryptSecret("foo")
            assert exc_info == "This data is not Base64!"
    @patch(target="encrypt.encryption.db.getSecretFromDb")
    def test_decrypt_with_not_base64(self, mock_getSecret : Mock):
        mock_getSecret.return_value = "foo"
        with pytest.raises(Exception) as exc_info:
            decryptSecret("foo")
            assert exc_info == "This data is not Base64!"
    @patch(target="encrypt.encryption.db.getSecretFromDb")
    def test_decrypt_with_base64(self, mock_getSecret : Mock):
        mock_getSecret.return_value = "YXNk"
        expected = "asd"
        actual = decryptSecret("foo")
        assert expected == actual

