import email
import unittest, os
from project import db,create_app
from project.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):
        db.create_all(app=create_app())

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
       # u = User(username='susan')
        u = User(id = "00000000", email="suzen@suzen");
        u.password("cat")
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)