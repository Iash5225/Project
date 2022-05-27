import unittest
from project import create_app, db
from project.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
        LastUser = last_item = User.query.order_by(User.id.desc()).first()
        
        U1 = User(id = LastUser.id +1, email="iash@iash", name ="iash", password = "1234");
        U2 = User(id = LastUser.id +2, email="jp@jp", name ="jp", password = "ilikeCITS3403");
        U3 = User(id = LastUser.id +3, email="david@david", name ="david", password = "idon'tlikeCITS3403");
        
        #u1 = User(id = LastUser.id +1, email="bob@bob", name ="bob", password = "1234");
        db.session.add(U1)
        db.session.add(U2)
        db.session.add(U3)
        db.session.commit()

    def tearDown(self):
        temp = User.query.order_by(User.id.desc()).first()
        lastid = temp.id
        User.query.filter_by(id=lastid).delete()
        User.query.filter_by(id=lastid-1).delete()
        User.query.filter_by(id=lastid-2).delete()
        db.session.commit()

    def test_password_hashing(self):
        temp = User.query.order_by(User.id.desc()).first()
        
        U1 = User.query.get(temp.id-2)
        U2 = User.query.get(temp.id-1)
        U3 = User.query.get(temp.id)
        
        ##Test should return True
        self.assertEqual(U1.name,"iash")
        self.assertEqual(U1.password,"1234")
        
        ##Test should return True
        self.assertEqual(U2.name,"jp")
        self.assertEqual(U2.password,"ilikeCITS3403")
        
        ##Test should return True
        self.assertEqual(U3.name,"david")
        self.assertEqual(U3.password,"idon'tlikeCITS3403")
        
        ##Test should return False
        self.assertEqual(U3.password,"test")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)