import unittest
from project import create_app, db
from project.models import Scores, User
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from werkzeug.security import generate_password_hash, check_password_hash
from time import sleep
from selenium.webdriver.common.by import By

class SystemTest(unittest.TestCase):
    driver = None
       
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if not self.driver:
          self.skipTest('Web browser not available')
        else:    
            app=create_app()
            self.app = app.test_client()     
            app.app_context().push()
            db.create_all()
            
            U1 = User(email="smith@smith",  password = generate_password_hash("1234", method='sha256'),name ="smith");
            S1 = Scores( userid = 1, score = 10)
        
            db.session.add(U1)
            db.session.add(S1)

            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')


    def tearDown(self):
        if self.driver:
            
            LastUser = User.query.order_by(User.id.desc()).first()
            LastScore = Scores.query.order_by(Scores.score_log_id.desc()).first()
            
            User.query.filter_by(id=LastUser.id).delete()
            User.query.filter_by(id=LastUser.id-1).delete()
        
            Scores.query.filter_by(score_log_id=LastScore.score_log_id).delete()
        
            db.session.commit()
            self.driver.close()            

    def test_signup(self):
        ##SIGN UP A USER
        temp = User.query.order_by(User.id.desc()).first()
        
        U1 = User.query.get(temp.id)
        
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
        
        self.driver.implicitly_wait(5)
                
        SignUpButton = self.driver.find_element_by_class_name("Login")
        SignUpButton.click()  

        sleep(2)

        ##to check if user typing in wrong password

        LoginButton = self.driver.find_element_by_class_name("Login")

        Email = self.driver.find_element_by_id('email')
        Email.send_keys('SystemTest@SystemTest')

        Password = self.driver.find_element_by_id('password')
        Password.send_keys('Wrong Password')

        sleep(2)
        
        LoginButton.click() 

        ErrorMessage = self.driver.find_element_by_id('errormessage')
        print(ErrorMessage.get_attribute('innerHTML'))
        sleep(2)

        #check login success
        #self.driver.implicitly_wait(5)
        #logout = self.driver.find_element_by_partial_link_text('Logout')
        #self.assertEqual(logout.get_attribute('innerHTML'), 'Logout Testy', msg='Logged in')
 
if __name__ == '__main__':
    unittest.main(verbosity=2)