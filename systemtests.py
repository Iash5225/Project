from lib2to3.pgen2 import driver
import unittest,os
from project import create_app, db
from project.models import Scores, User
from werkzeug.security import generate_password_hash, check_password_hash
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
basedir = os.path.abspath(os.path.dirname(__file__))
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options





class SystemTest(unittest.TestCase):
    driver = None
    
    
    def setUp(self):
        
        self.driver = webdriver.Chrome(executable_path="/mnt/c/Program Files/Google/Chrome/Application/chromedriver.exe")
        #self.driver.get('http://www.google.com')
        print('test')
    
        if not self.driver:
          self.skipTest('Web browser not available')
        else:
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
        self.assertEqual(U1.name,"iash")
        self.assertEqual(U1.email,"iash@iash")
        self.assertTrue(check_password_hash(U1.password, "1234"))
        
        self.driver.get('http://localhost:5000/signup')
        
        self.driver.implicitly_wait(5)
        
        Email = self.driver.find_element_by_class_name("email")
        Email.send_keys('SystemTest@SystemTest')
        
        Name = self.driver.find_element_by_class_name("name")
        Name.send_keys('SystemTest')
        
        Password = self.driver.find_element_by_class_name("password")
        Password.send_keys('PasswordTester')
        
        self.driver.implicitly_wait(5)
        
        SignUpButton = self.driver.find_element_by_class_name("Login")
        SignUpButton.click()
        
        #check login success
        #self.driver.implicitly_wait(5)
        #logout = self.driver.find_element_by_partial_link_text('Logout')
       # self.assertEqual(logout.get_attribute('innerHTML'), 'Logout Testy', msg='Logged in')

        
if __name__ == '__main__':
    unittest.main(verbosity=2)