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
        assert self.driver.current_url == 'https://sandbox.moodledemo.net/'
        

    def test_2(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("teacher")
        password.send_keys("wrongpass")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/div/div[1]')
        assert errorNotification.text == "Invalid login, please try again"


    def test_3(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("notteacher")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/div/div[1]')
        assert errorNotification.text == "Invalid login, please try again"


    def test_4(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("notteacher")
        password.send_keys("wrongpass")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div/div/div/div[1]')
        assert errorNotification.text == "Invalid login, please try again"
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()