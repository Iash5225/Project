import unittest
from project import create_app, db
from project.models import Scores, User
from werkzeug.security import generate_password_hash, check_password_hash

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
        
        U1 = User(email="iash@iash", name ="iash", password = generate_password_hash("1234", method='sha256'));
        U2 = User(email="jp@jp", name ="jp", password = generate_password_hash("ilikeCITS3403", method='sha256'));
        U3 = User(email="david@david", name ="david", password = generate_password_hash("idon'tlikeCITS3403", method='sha256'));
        
        S1 = Scores( userid = 1, score = 10)
        S2 = Scores( userid = 2, score = 20)
        S3 = Scores( userid = 3, score = 30)
        
        db.session.add(U1)
        db.session.add(U2)
        db.session.add(U3)
        db.session.add(S1)
        db.session.add(S2)
        db.session.add(S3)
        
        db.session.commit()

    def tearDown(self):
        LastUser = User.query.order_by(User.id.desc()).first()
        LastScore = Scores.query.order_by(Scores.score_log_id.desc()).first()
            
        User.query.filter_by(id=LastUser.id).delete()
        User.query.filter_by(id=LastUser.id-1).delete()
        User.query.filter_by(id=LastUser.id-2).delete()
        
        Scores.query.filter_by(score_log_id=LastScore.score_log_id).delete()
        Scores.query.filter_by(score_log_id=LastScore.score_log_id-1).delete()
        Scores.query.filter_by(score_log_id=LastScore.score_log_id-2).delete()
        
        db.session.commit()

    def test_users(self):
        temp = User.query.order_by(User.id.desc()).first()
        
        U1 = User.query.get(temp.id-2)
        U2 = User.query.get(temp.id-1)
        U3 = User.query.get(temp.id)
        
        ##Test should return True
        self.assertEqual(U1.name,"iash")
        self.assertEqual(U1.email,"iash@iash")
        self.assertTrue(check_password_hash(U1.password, "1234"))
        
        ##Test should return True
        self.assertEqual(U2.name,"jp")
        self.assertEqual(U2.email,"jp@jp")
        self.assertTrue(check_password_hash(U2.password, "ilikeCITS3403"))
        
        ##Test should return True
        self.assertEqual(U3.name,"david")
        self.assertEqual(U3.email,"david@david")
        self.assertTrue(check_password_hash(U3.password, "idon'tlikeCITS3403"))
        
        ##Test False values
        self.assertNotEqual(U1.name,"tim")
        self.assertNotEqual(U2.email,"bob@builder")
        self.assertNotEqual(U3.password,"test")
        
    def test_scores(self):
        temp = Scores.query.order_by(Scores.score_log_id.desc()).first()
        
        S1 = Scores.query.get(temp.score_log_id-2)
        S2 = Scores.query.get(temp.score_log_id-1)
        S3 = Scores.query.get(temp.score_log_id)

        ##Test should return True
        self.assertEqual(S1.userid,1)
        self.assertEqual(S1.score,10)
        
        ##Test should return True
        self.assertEqual(S2.userid,2)
        self.assertEqual(S2.score,20)
        
        ##Test should return True
        self.assertEqual(S3.userid,3)
        self.assertEqual(S3.score,30)
        
        ##Test False values
        self.assertNotEqual(S2.userid,6)
        self.assertNotEqual(S3.score,100)
if __name__ == '__main__':
    unittest.main(verbosity=2)