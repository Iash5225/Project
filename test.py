import unittest
from project import create_app, db
from project.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
        u1 = User(id = 2, email="bob@bob", name ="bob", password = "1234");
        db.session.add(u1)
        db.session.commit()

    def tearDown(self):
        User.query.filter_by(id=2).delete()
        db.session.commit()
       # db.session.remove()
       #  db.drop_all()

    def test_password_hashing(self):
        u = User.query.get('2')
        name = u.name
        password = u.password
        self.assertEqual(password,"1234")
        self.assertEqual(name,"bob")

        
if __name__ == '__main__':
    unittest.main(verbosity=2)