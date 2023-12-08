import random
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.vars = {}

        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        usernameInput = self.driver.find_element(By.NAME,"username")
        passwordInput = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        usernameInput.clear()
        usernameInput.send_keys("admin")
        passwordInput.send_keys("sandbox")    
        submitBtn.click()
        time.sleep(1)

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self): #done
        myCourses = self.driver.find_elements(By.CLASS_NAME,'nav-item')
        myCourses[2].click()
        buttons = self.driver.find_elements(By.CLASS_NAME,"singlebutton")
        buttons[1].click()
        time.sleep(1)
        fullname = self.driver.find_element(By.XPATH,'//*[@id="id_fullname"]')
        fullname.clear()
        fullname.send_keys("Software testing")
        time.sleep(1)

        shortName = self.driver.find_element(By.XPATH,'//*[@id="id_shortname"]')
        shortName.clear()
        shortName.send_keys("Testing" + str(random.randint(0,199)))
        time.sleep(1)
        saveBtn = self.driver.find_element(By.XPATH,'//*[@id="id_saveanddisplay"]')
        saveBtn.click()
        time.sleep(1)
    
        assert self.driver.current_url.__contains__('https://sandbox.moodledemo.net/course/view.php')
        

    def test_2(self): #done
        myCourses = self.driver.find_elements(By.CLASS_NAME,'nav-item')
        myCourses[2].click()
        buttons = self.driver.find_elements(By.CLASS_NAME,"singlebutton")
        buttons[1].click()
        time.sleep(1)
        fullname = self.driver.find_element(By.XPATH,'//*[@id="id_fullname"]')
        fullname.clear()
        fullname.send_keys("Software testing")
        time.sleep(1)

        saveBtn = self.driver.find_element(By.XPATH,'//*[@id="id_saveanddisplay"]')
        saveBtn.click()
        time.sleep(5)
    
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/course/edit.php'
        


    def test_3(self): #done
        myCourses = self.driver.find_elements(By.CLASS_NAME,'nav-item')
        myCourses[2].click()
        buttons = self.driver.find_elements(By.CLASS_NAME,"singlebutton")
        buttons[1].click()
        time.sleep(1)

        shortName = self.driver.find_element(By.XPATH,'//*[@id="id_shortname"]')
        shortName.clear()
        shortName.send_keys("Testing" + str(random.randint(0,199)))
        time.sleep(1)
        saveBtn = self.driver.find_element(By.XPATH,'//*[@id="id_saveanddisplay"]')
        saveBtn.click()
        time.sleep(1)
    
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/course/edit.php'
        

    def test_4(self): #done
        myCourses = self.driver.find_elements(By.CLASS_NAME,'nav-item')
        myCourses[2].click()
        buttons = self.driver.find_elements(By.CLASS_NAME,"singlebutton")
        buttons[1].click()
        time.sleep(1)

        saveBtn = self.driver.find_element(By.XPATH,'//*[@id="id_saveanddisplay"]')
        saveBtn.click()
        time.sleep(1)
    
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/course/edit.php'

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()