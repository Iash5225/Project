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

        sleep(5)
        
        LoginButton.click() 

        WelcomeMessage = self.driver.find_element(By.ID,'welcomemessage')
        self.assertEqual(WelcomeMessage.get_attribute('innerHTML'),"\n  Welcome, bob!\n  \n")
        sleep(5)
        
    def test_unsuccessfullogin(self):
            ##Assuming user has an account, and is inputting an incorrect password
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

        sleep(5)
        
        LoginButton.click() 

        ErrorMessage = self.driver.find_element(By.ID,'errormessage')
        
        ##Test should return True
        self.assertEqual(ErrorMessage.get_attribute('innerHTML'),'Please check your login details and try again.')
        sleep(5)
    
    def test_correctsignup(self):
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
        
        temp = User.query.order_by(User.id.desc()).first()  
        U1 = User.query.get(temp.id)
        
        ##Test should return True
        self.assertEqual(U1.name,'SystemTest')
        self.assertEqual(U1.email,'SystemTest@SystemTest')
        self.assertTrue(check_password_hash(U1.password, 'PasswordTester'))
        sleep(5)
        
    def test_incorrectsignup(self):
         ##Incorrectly signing up by already having an account associated with the email
        U2 = User(email="jane@jane", password = generate_password_hash("1234", method='sha256'),name ="jane");

        db.session.add(U2)
        db.session.commit()
        
        self.driver.get('http://localhost:5000/signup')
        
        self.driver.implicitly_wait(5)
        
        Email = self.driver.find_element(By.ID,'email')
        Email.send_keys('jane@jane')
        
        Name = self.driver.find_element(By.ID,'name')
        Name.send_keys('jane')
        
        Password = self.driver.find_element(By.ID,'password')
        Password.send_keys('1234')
        
        self.driver.implicitly_wait(5)
                
        SignUpButton = self.driver.find_element(by=By.CLASS_NAME, value="Login")
        SignUpButton.click()  
        sleep(5)
        
        ErrorMessage = self.driver.find_element(By.ID,'errormessage')
        
        ##Test should return True
        self.assertTrue("Email address already exists." in ErrorMessage.get_attribute('innerHTML'))
        self.assertEqual(self.driver.current_url,'http://localhost:5000/signup')
        sleep(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)