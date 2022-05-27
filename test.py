
from flask import Flask
import unittest, os
from project import create_app, db,create_TEMPapp
from project.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
       # u1 = User(id = 8, email="caleb@caleb", name ="caleb", password = "dog");
      #  db.session.add(u1)
        db.session.commit()

    # def tearDown(self):
      #  User.query.filter_by(id=5).delete()
      #  db.session.commit()
       # db.session.remove()
      #  db.drop_all()

    def test_password_hashing(self):
       # u = User(username='susan')
        u = User.query.get('5')
        str2 = u.password
        self.assertEqual(str2,"cat")
        #self.assertEqual("cat","cat")

        
if __name__ == '__main__':
    unittest.main(verbosity=2)