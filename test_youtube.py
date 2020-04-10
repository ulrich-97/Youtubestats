import unittest 
import docstrings

class TestAccount(unittest.TestCase):
    def test_init(self, edit):
        pass
    
    def test_register(self, create_user, create_password, create_email,
                 create_phonenum, login):
        pass 
    
    def test_login(self, username_login, password_login):
        pass