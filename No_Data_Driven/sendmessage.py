import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestSendMessage(unittest.TestCase):
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
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        messageIcon = self.driver.find_element(By.CSS_SELECTOR,'#usernavigation > div:nth-child(4)')
        messageIcon.click()

        time.sleep(4)
        selectUser = self.driver.find_element(By.CSS_SELECTOR,'.py-0.px-2.d-flex.list-group-item.list-group-item-action.align-items-center')
        selectUser.click()
        time.sleep(4)

        inputMessage = self.driver.find_element(By.CSS_SELECTOR,'.p-sm-2>.d-flex.mt-sm-1>textarea')
        inputMessage.send_keys('Nhap vip')
        time.sleep(1)
        
        textContainer = self.driver.find_element(By.CSS_SELECTOR,'*>div[data-region="day-messages-container"]')
        prevChildren = textContainer.get_property("childElementCount")

        buttonSend = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div[4]/div[1]/div[1]/div[2]/div/button[2]')
        buttonSend.click()
        time.sleep(3)
        
        assert prevChildren + 1 == textContainer.get_property("childElementCount")

    def test_2(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
        
        messageIcon = self.driver.find_element(By.CSS_SELECTOR,'#usernavigation > div:nth-child(4)')
        messageIcon.click()

        time.sleep(4)
        selectUser = self.driver.find_element(By.CSS_SELECTOR,'.py-0.px-2.d-flex.list-group-item.list-group-item-action.align-items-center')
        selectUser.click()
        time.sleep(4)

        inputMessage = self.driver.find_element(By.CSS_SELECTOR,'.p-sm-2>.d-flex.mt-sm-1>textarea')
        inputMessage.send_keys('Tuong oi')
        time.sleep(1)
        
        textContainer = self.driver.find_element(By.CSS_SELECTOR,'*>div[data-region="day-messages-container"]')
        prevChildren = textContainer.get_property("childElementCount")

        buttonSend = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div[4]/div[1]/div[1]/div[2]/div/button[2]')
        buttonSend.click()
        time.sleep(3)
        
        assert prevChildren + 1 == textContainer.get_property("childElementCount")


    def test_3(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)

        messageIcon = self.driver.find_element(By.CSS_SELECTOR,'#usernavigation > div:nth-child(4)')
        messageIcon.click()

        time.sleep(4)
        selectUser = self.driver.find_element(By.CSS_SELECTOR,'.py-0.px-2.d-flex.list-group-item.list-group-item-action.align-items-center')
        selectUser.click()
        time.sleep(4)

        inputMessage = self.driver.find_element(By.CSS_SELECTOR,'.p-sm-2>.d-flex.mt-sm-1>textarea')
        # inputMessage.send_keys(None)
        time.sleep(1)
        
        textContainer = self.driver.find_element(By.CSS_SELECTOR,'*>div[data-region="day-messages-container"]')
        prevChildren = textContainer.get_property("childElementCount")

        buttonSend = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div[4]/div[1]/div[1]/div[2]/div/button[2]')
        buttonSend.click()
        time.sleep(3)
        
        assert prevChildren == textContainer.get_property("childElementCount")


        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()