import unittest
from project import create_app, db
from project.models import Scores, User
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from werkzeug.security import generate_password_hash, check_password_hash
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SystemTest(unittest.TestCase):
    driver = None
       
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        if not self.driver:
          self.skipTest('Web browser not available')
        else:    
            app=create_app()
            self.app = app.test_client()     
            app.app_context().push()
            db.create_all()
        
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')


    def tearDown(self):
        if self.driver:
            
            LastUser = User.query.order_by(User.id.desc()).first()
            LastScore = Scores.query.order_by(Scores.score_log_id.desc()).first()
            
            User.query.filter_by(id=LastUser.id).delete()
        
            db.session.commit()
            self.driver.close()            

    def test_successfullogin(self):
          ##Assuming the user has signed up and is now correctly login in 
        U1 = User(email="bob@bob",  password = generate_password_hash("1234", method='sha256'),name ="bob");

        db.session.add(U1)
        db.session.commit()
          
        self.driver.get('http://localhost:5000/login')
        
        self.driver.implicitly_wait(5)
        
        LoginButton = self.driver.find_element(by=By.CLASS_NAME, value="Login")

        Email = self.driver.find_element(By.ID,'email')
        Email.send_keys('bob@bob')

        Password = self.driver.find_element(By.ID,'password')
        Password.send_keys('1234')

        sleep(1)
        
        LoginButton.click() 

        WelcomeMessage = self.driver.find_element(By.ID,'welcomemessage')
        self.assertEqual(WelcomeMessage.get_attribute('innerHTML'),"\n  Welcome, bob!\n  \n")
        sleep(2)
        
    def test_unsuccessfullogin(self):
            ##Assuming the user has signed up and is now incorrectly login in 
        U2 = User(email="jane@jane", password = generate_password_hash("1234", method='sha256'),name ="jane");

        db.session.add(U2)
        db.session.commit()
          
        self.driver.get('http://localhost:5000/login')
        
        self.driver.implicitly_wait(5)
        
        LoginButton = self.driver.find_element(by=By.CLASS_NAME, value="Login")

        Email = self.driver.find_element(By.ID,'email')
        Email.send_keys('jane@jane')

        Password = self.driver.find_element(By.ID,'password')
        Password.send_keys('4567')

        sleep(1)
        
        LoginButton.click() 

        ErrorMessage = self.driver.find_element(By.ID,'errormessage')
        self.assertEqual(ErrorMessage.get_attribute('innerHTML'),'Please check your login details and try again.')
        sleep(1)
    
    def test_signup(self):
        self.driver.get('http://localhost:5000/signup')
        
        self.driver.implicitly_wait(5)
        
        Email = self.driver.find_element(By.ID,'email')
        Email.send_keys('SystemTest@SystemTest')
        
        Name = self.driver.find_element(By.ID,'name')
        Name.send_keys('SystemTest')
        
        Password = self.driver.find_element(By.ID,'password')
        Password.send_keys('PasswordTester')
        
        self.driver.implicitly_wait(5)
                
        SignUpButton = self.driver.find_element(by=By.CLASS_NAME, value="Login")
        SignUpButton.click()  
        sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)