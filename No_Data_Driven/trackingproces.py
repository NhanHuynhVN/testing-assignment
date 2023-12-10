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
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.execute_script("window.scrollTo(0,980)")
        self.driver.find_element(By.ID, "id_completion_1").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()
        assert self.driver.current_url == 'https://school.moodledemo.net/course/view.php?id=51'
        

    def test_2(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.execute_script("window.scrollTo(0,669)")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .form-check-label").click()
        self.driver.find_element(By.ID, "id_completion_1").click()
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        dropdown.find_element(By.XPATH, "//option[. = '30']").click()
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()
        assert self.driver.current_url == 'https://school.moodledemo.net/course/view.php?id=51'


    def test_3(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.execute_script("window.scrollTo(0,656)")
        element = self.driver.find_element(By.ID, "collapseElement-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        self.driver.find_element(By.ID, "id_completion_1").click()
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        dropdown.find_element(By.XPATH, "//option[. = '2']").click()
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        dropdown.find_element(By.XPATH, "//option[. = 'November']").click()
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_year")
        dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()
        assert self.driver.current_url == 'https://school.moodledemo.net/course/view.php?id=51'


    def test_4(self): #done
        self.driver.get("https://school.moodledemo.net/mod/resource/view.php?id=949")
        self.driver.set_window_size(1292, 836)
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,507)")
        self.driver.find_element(By.ID, "collapseElement-4").click()
        self.driver.find_element(By.ID, "id_completion_1").click()
        self.driver.find_element(By.ID, "id_completionexpected_enabled").click()
        self.driver.find_element(By.ID, "id_completionexpected_year").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_year")
        dropdown.find_element(By.XPATH, "//option[. = '2020']").click()
        self.driver.find_element(By.ID, "id_completionexpected_day").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_day")
        dropdown.find_element(By.XPATH, "//option[. = '29']").click()
        self.driver.find_element(By.ID, "id_completionexpected_month").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_month")
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        self.driver.find_element(By.ID, "id_completionexpected_hour").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_hour")
        dropdown.find_element(By.XPATH, "//option[. = '09']").click()
        self.driver.find_element(By.ID, "id_completionexpected_minute").click()
        dropdown = self.driver.find_element(By.ID, "id_completionexpected_minute")
        dropdown.find_element(By.XPATH, "//option[. = '15']").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".drawer-right-toggle > .btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        
        assert self.driver.current_url == 'https://school.moodledemo.net/course/view.php?id=51'

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()