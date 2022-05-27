import unittest
from project import create_app, db
from project.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
        LastUser = User.query.order_by(User.id.desc()).first()
        
        U1 = User(id = LastUser.id +1, email="iash@iash", name ="iash", password = "1234");
        U2 = User(id = LastUser.id +2, email="jp@jp", name ="jp", password = "ilikeCITS3403");
        U3 = User(id = LastUser.id +3, email="david@david", name ="david", password = "idon'tlikeCITS3403");
        
        db.session.add(U1)
        db.session.add(U2)
        db.session.add(U3)
        db.session.commit()

    def tearDown(self):
        temp = User.query.order_by(User.id.desc()).first()
        User.query.filter_by(id=temp.id).delete()
        User.query.filter_by(id=temp.id-1).delete()
        User.query.filter_by(id=temp.id-2).delete()
        db.session.commit()

    def test_users(self):
        temp = User.query.order_by(User.id.desc()).first()
        
        U1 = User.query.get(temp.id-2)
        U2 = User.query.get(temp.id-1)
        U3 = User.query.get(temp.id)
        
        ##Test should return True
        self.assertEqual(U1.name,"iash")
        self.assertEqual(U1.email,"iash@iash")
        self.assertEqual(U1.password,"1234")
        
        ##Test should return True
        self.assertEqual(U2.name,"jp")
        self.assertEqual(U2.email,"jp@jp")
        self.assertEqual(U2.password,"ilikeCITS3403")
        
        ##Test should return True
        self.assertEqual(U3.name,"david")
        self.assertEqual(U3.email,"david@david")
        self.assertEqual(U3.password,"idon'tlikeCITS3403")
        
        ##Test False values
        self.assertNotEqual(U1.name,"tim")
        self.assertNotEqual(U2.email,"bob@builder")
        self.assertNotEqual(U3.password,"test")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)