import unittest
from project import create_app, db
from project.models import Scores, User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from sqlalchemy import select
import numpy as np

today = date.today()

class UserModelCase(unittest.TestCase):
    def setUp(self):        
        app = create_app()      
        self.app = app.test_client()     
        app.app_context().push()
        db.create_all
        
        U1 = User(email="iash@iash", password = generate_password_hash("1234", method='sha256'),name ="iash",highscore =1000,lastplayed= today);
        U2 = User(email="jp@jp", password = generate_password_hash("ilikeCITS3403", method='sha256'),name ="jp",highscore =950,lastplayed= today);
        U3 = User(email="david@david",  password = generate_password_hash("idon'tlikeCITS3403", method='sha256'),name ="david",highscore =900,lastplayed= today);
        U4 = User(email="liam@liam",  password = generate_password_hash("test", method='sha256'),name ="liam",highscore =850,lastplayed= today);
        U5 = User(email="emma@emma",  password = generate_password_hash("test", method='sha256'),name ="emma",highscore =800,lastplayed= today);
        U6 = User(email="oliver@oliver",  password = generate_password_hash("test", method='sha256'),name ="oliver",highscore =750,lastplayed= today);
        U7 = User(email="amelia@amelia",  password = generate_password_hash("test", method='sha256'),name ="amelia",highscore =700,lastplayed= today);
        U8 = User(email="james@james",  password = generate_password_hash("test", method='sha256'),name ="james",highscore =650,lastplayed= today);
        U9= User(email="sophia@sophia",  password = generate_password_hash("test", method='sha256'),name ="sophia",highscore =600,lastplayed= today);
        U10 = User(email="benjamin@benjamin",  password = generate_password_hash("test", method='sha256'),name ="benjamin",highscore =550,lastplayed= today);
        
        
        S1 = Scores( userid = 1, score = 10)
        S2 = Scores( userid = 2, score = 20)
        S3 = Scores( userid = 3, score = 30)
        
        db.session.add(U1)
        db.session.add(U2)
        db.session.add(U3)
        db.session.add(U4)
        db.session.add(U5)
        db.session.add(U6)
        db.session.add(U7)
        db.session.add(U8)
        db.session.add(U9)
        db.session.add(U10)
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
        User.query.filter_by(id=LastUser.id-3).delete()
        User.query.filter_by(id=LastUser.id-4).delete()
        User.query.filter_by(id=LastUser.id-5).delete()
        User.query.filter_by(id=LastUser.id-6).delete()
        User.query.filter_by(id=LastUser.id-7).delete()
        User.query.filter_by(id=LastUser.id-8).delete()
        User.query.filter_by(id=LastUser.id-9).delete()
        
        Scores.query.filter_by(score_log_id=LastScore.score_log_id).delete()
        Scores.query.filter_by(score_log_id=LastScore.score_log_id-1).delete()
        Scores.query.filter_by(score_log_id=LastScore.score_log_id-2).delete()
        
        db.session.commit()

    def test_users(self):
        temp = User.query.order_by(User.id.desc()).first()
        
        U1 = User.query.get(temp.id-9)
        U2 = User.query.get(temp.id-8)
        U3 = User.query.get(temp.id-7)
        U4 = User.query.get(temp.id-6)
        U5 = User.query.get(temp.id-5)
        U6 = User.query.get(temp.id-4)
        U7 = User.query.get(temp.id-3)
        U8 = User.query.get(temp.id-2)
        U9 = User.query.get(temp.id-1)
        U10 = User.query.get(temp.id)
        
        ##Test should return True
        self.assertEqual(U1.name,"iash")
        self.assertEqual(U1.email,"iash@iash")
        self.assertTrue(check_password_hash(U1.password, "1234"))
        self.assertEqual(U1.highscore,1000)
        self.assertEqual(U1.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U2.name,"jp")
        self.assertEqual(U2.email,"jp@jp")
        self.assertTrue(check_password_hash(U2.password, "ilikeCITS3403"))
        self.assertEqual(U2.highscore,950)
        self.assertEqual(U2.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U3.name,"david")
        self.assertEqual(U3.email,"david@david")
        self.assertTrue(check_password_hash(U3.password, "idon'tlikeCITS3403"))
        self.assertEqual(U3.highscore,900)
        self.assertEqual(U3.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U4.name,"liam")
        self.assertEqual(U4.email,"liam@liam")
        self.assertTrue(check_password_hash(U4.password, "test"))
        self.assertEqual(U4.highscore,850)
        self.assertEqual(U4.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U5.name,"emma")
        self.assertEqual(U5.email,"emma@emma")
        self.assertTrue(check_password_hash(U5.password, "test"))
        self.assertEqual(U5.highscore,800)
        self.assertEqual(U5.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U6.name,"oliver")
        self.assertEqual(U6.email,"oliver@oliver")
        self.assertTrue(check_password_hash(U6.password, "test"))
        self.assertEqual(U6.highscore,750)
        self.assertEqual(U6.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U7.name,"amelia")
        self.assertEqual(U7.email,"amelia@amelia")
        self.assertTrue(check_password_hash(U7.password, "test"))
        self.assertEqual(U7.highscore,700)
        self.assertEqual(U7.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U8.name,"james")
        self.assertEqual(U8.email,"james@james")
        self.assertTrue(check_password_hash(U8.password, "test"))
        self.assertEqual(U8.highscore,650)
        self.assertEqual(U8.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U9.name,"sophia")
        self.assertEqual(U9.email,"sophia@sophia")
        self.assertTrue(check_password_hash(U9.password, "test"))
        self.assertEqual(U9.highscore,600)
        self.assertEqual(U9.lastplayed,today)
        
        ##Test should return True
        self.assertEqual(U10.name,"benjamin")
        self.assertEqual(U10.email,"benjamin@benjamin")
        self.assertTrue(check_password_hash(U10.password, "test"))
        self.assertEqual(U10.highscore,550)
        self.assertEqual(U10.lastplayed,today)            
        
        ##Test False values
        self.assertNotEqual(U1.name,"tim")
        self.assertNotEqual(U2.email,"bob@builder")
        self.assertNotEqual(U3.password,"test")
        self.assertNotEqual(U3.highscore,55)
        
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
    
    def test_leaderboard(self):
        leaderboard = db.session.execute(select(User.highscore, User.name)
                                    .order_by(User.highscore.desc(), User.name)
                                    .limit(10))

        leaderboard_names = []
        leaderboard_scores = []
        
        Testleaderboard_name = np.array(['iash', 'jp', 'david', 'liam', 'emma', 'oliver', 'amelia', 'james', 'sophia', 'benjamin'])
        Testleaderboard_scores = np.array([1000, 950, 900, 850, 800, 750, 700, 650, 600, 550])
        for row in leaderboard:
            leaderboard_names.append(row.name)
            leaderboard_scores.append(row.highscore)
        self.assertTrue(np.array_equal(np.array(leaderboard_names),Testleaderboard_name))
        self.assertTrue(np.array_equal(np.array(leaderboard_scores),Testleaderboard_scores))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)