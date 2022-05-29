import unittest,os
from project import create_app, db
from project.models import Scores, User
from selenium import webdriver
#basedir = os.path.abspath(os.path.dirname(__file__))
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from werkzeug.security import generate_password_hash, check_password_hash

import hashlib
from time import sleep

import unittest

#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SystemTest(unittest.TestCase):
    driver = None
       
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if not self.driver:
          self.skipTest('Web browser not available')
        else:    
            self.app = app.test_client()     
            app.app_context().push()
            db.create_all(app=create_app())
        
            U1 = User(email="smith@smith",  password = generate_password_hash("1234", method='sha256'),name ="smith");
            U2 = User(email="Z@Z", password = generate_password_hash("ilikeCITS3403", method='sha256'),name ="Z");
            U3 = User(email="D@D",password = generate_password_hash("idon'tlikeCITS3403", method='sha256'), name ="D");
        
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
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')


    def tearDown(self):
        if self.driver:
            self.driver.close()
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
        self.assertEqual(U1.name,"smith")
        self.assertEqual(U1.email,"smith@smith")
        self.assertTrue(check_password_hash(U1.password, "1234"))
        
        self.driver.get('http://localhost:5000/signup')
        
        self.driver.implicitly_wait(5)
        
        #Email = self.driver.find_element(by=By.CLASS_NAME, value="email")
        Email = self.driver.find_element_by_id('email')
        Email.send_keys('SystemTest@SystemTest')
        
        #Name = self.driver.find_element(by=By.CLASS_NAME, value="name")
        Name = self.driver.find_element_by_id('name')
        Name.send_keys('SystemTest')
        
       # Password = self.driver.find_element(by=By.CLASS_NAME, value="password")
        Password = self.driver.find_element_by_id('password')
        Password.send_keys('PasswordTester')
        
       # self.driver.implicitly_wait(5)
        sleep(10)
        
        SignUpButton = self.driver.find_element_by_class_name("Login")
        SignUpButton.click()
        
        #check login success
        #self.driver.implicitly_wait(5)
        #logout = self.driver.find_element_by_partial_link_text('Logout')
       # self.assertEqual(logout.get_attribute('innerHTML'), 'Logout Testy', msg='Logged in')

        
if __name__ == '__main__':
    unittest.main(verbosity=2)