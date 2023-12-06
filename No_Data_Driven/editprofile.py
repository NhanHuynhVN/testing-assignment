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

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("teacher")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        
        avatarIcon = self.driver.find_element(By.XPATH,'//*[@id="user-menu-toggle"]')
        avatarIcon.click()
        time.sleep(1)
        selectProfile = self.driver.find_element(By.XPATH,'//*[@id="carousel-item-main"]/a[1]')
        selectProfile.click()
        time.sleep(1)

        selectEditProfile = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/section[1]/div/ul/li[1]/span/a')
        selectEditProfile.click()
        time.sleep(1)

        fname = self.driver.find_element(By.XPATH,'//*[@id="id_firstname"]')
        fname.clear()
        fname.send_keys("Tuong")
        time.sleep(1)

        lname = self.driver.find_element(By.XPATH,'//*[@id="id_lastname"]')
        lname.clear()
        lname.send_keys("Lau") 
        time.sleep(1)

        updateBtn = self.driver.find_element(By.XPATH,'//*[@id="id_submitbutton"]')
        updateBtn.click()
        time.sleep(1)
        alert = self.driver.find_element(By.XPATH,'//*[@id="user-notifications"]/div')
        assert alert.text != None
        

    def test_2(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("teacher")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        
        avatarIcon = self.driver.find_element(By.XPATH,'//*[@id="user-menu-toggle"]')
        avatarIcon.click()
        time.sleep(1)
        selectProfile = self.driver.find_element(By.XPATH,'//*[@id="carousel-item-main"]/a[1]')
        selectProfile.click()
        time.sleep(1)

        selectEditProfile = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/section[1]/div/ul/li[1]/span/a')
        selectEditProfile.click()
        time.sleep(1)

        fname = self.driver.find_element(By.XPATH,'//*[@id="id_firstname"]')
        fname.clear()
        fname.send_keys("Tuong")
        time.sleep(1)

        lname = self.driver.find_element(By.XPATH,'//*[@id="id_lastname"]')
        lname.clear()
        time.sleep(1)

        updateBtn = self.driver.find_element(By.XPATH,'//*[@id="id_submitbutton"]')
        updateBtn.click()
        time.sleep(1)
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/user/edit.php?id=3&returnto=profile'


    def test_3(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("teacher")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        
        avatarIcon = self.driver.find_element(By.XPATH,'//*[@id="user-menu-toggle"]')
        avatarIcon.click()
        time.sleep(1)
        selectProfile = self.driver.find_element(By.XPATH,'//*[@id="carousel-item-main"]/a[1]')
        selectProfile.click()
        time.sleep(1)

        selectEditProfile = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/section[1]/div/ul/li[1]/span/a')
        selectEditProfile.click()
        time.sleep(1)

        fname = self.driver.find_element(By.XPATH,'//*[@id="id_firstname"]')
        fname.clear()
        time.sleep(1)

        lname = self.driver.find_element(By.XPATH,'//*[@id="id_lastname"]')
        lname.clear()
        lname.send_keys("Lau") 
        time.sleep(1)

        updateBtn = self.driver.find_element(By.XPATH,'//*[@id="id_submitbutton"]')
        updateBtn.click()
        time.sleep(1)
        
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/user/edit.php?id=3&returnto=profile'


    def test_4(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("teacher")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        
        avatarIcon = self.driver.find_element(By.XPATH,'//*[@id="user-menu-toggle"]')
        avatarIcon.click()
        time.sleep(1)
        selectProfile = self.driver.find_element(By.XPATH,'//*[@id="carousel-item-main"]/a[1]')
        selectProfile.click()
        time.sleep(1)

        selectEditProfile = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/section[1]/div/ul/li[1]/span/a')
        selectEditProfile.click()
        time.sleep(1)

        fname = self.driver.find_element(By.XPATH,'//*[@id="id_firstname"]')
        fname.clear()
        time.sleep(1)

        lname = self.driver.find_element(By.XPATH,'//*[@id="id_lastname"]')
        lname.clear()
        time.sleep(1)

        updateBtn = self.driver.find_element(By.XPATH,'//*[@id="id_submitbutton"]')
        updateBtn.click()
        time.sleep(1)
        
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/user/edit.php?id=3&returnto=profile'

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()