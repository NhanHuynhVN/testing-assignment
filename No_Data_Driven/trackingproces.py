import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


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
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.execute_script("window.scrollTo(0,980)")
        self.driver.find_element(By.LINK_TEXT, "Completion conditions").click()
        self.driver.find_element(By.ID, "id_completion_1").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()
        

    def test_2(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.execute_script("window.scrollTo(0,980)")
        self.driver.find_element(By.LINK_TEXT, "Completion conditions").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completion_1").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '30']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_submitbutton2").click()


    def test_3(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.execute_script("window.scrollTo(0,980)")
        self.driver.find_element(By.LINK_TEXT, "Completion conditions").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completion_1").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '2']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = 'November']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_year")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_submitbutton2").click()


    def test_4(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.execute_script("window.scrollTo(0,980)")
        self.driver.find_element(By.LINK_TEXT, "Completion conditions").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completion_1").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_year")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '2020']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '29']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_submitbutton2").click()

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()