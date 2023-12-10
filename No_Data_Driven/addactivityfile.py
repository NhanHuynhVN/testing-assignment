import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestSiteHomeSetting(unittest.TestCase):
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
        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        self.driver.set_window_size(2560, 1415)
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Add an activity or resource\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#all-5 .option:nth-child(8) .optionicon > .icon").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("File activity")
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Add new file activity</p>'}", element)
        self.driver.find_element(By.CSS_SELECTOR, ".dndupload-message .fa").click()
        self.driver.find_element(By.NAME, "repo_upload_file").click()
        self.driver.find_element(By.NAME, "repo_upload_file").send_keys("/Users/nguyenkhanh/Documents/Chap_3_AI.pdf")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_2(self): #done
        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        self.driver.set_window_size(2560, 1415)
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Add an activity or resource\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#all-5 .option:nth-child(8) .optionicon > .icon").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Add new file activity</p>'}", element)
        self.driver.find_element(By.CSS_SELECTOR, ".dndupload-message .fa").click()
        self.driver.find_element(By.NAME, "repo_upload_file").click()
        self.driver.find_element(By.NAME, "repo_upload_file").send_keys("/Users/nguyenkhanh/Documents/Chap_3_AI.pdf")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()


    def test_3(self): #done
        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        self.driver.set_window_size(2560, 1415)
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Add an activity or resource\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#all-5 .option:nth-child(8) .optionicon > .icon").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("File activity")
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH, "//body[@id=\'tinymce\']/p").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Add new file activity</p>'}", element)
        self.driver.find_element(By.XPATH, "//input[@id=\'id_submitbutton2\']").click()

    def test_4(self): #done
        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        self.driver.set_window_size(2560, 1415)
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Add an activity or resource\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#all-5 .option:nth-child(8) .optionicon > .icon").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("File activity")
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Add new file activity</p>'}", element)
        self.driver.find_element(By.CSS_SELECTOR, ".dndupload-message .fa").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_5(self): #done
        self.driver.get("https://school.moodledemo.net/course/view.php?id=51")
        self.driver.set_window_size(2560, 1415)
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Add an activity or resource\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#all-5 .option:nth-child(8) .optionicon > .icon").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("File activity")
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Add new file activity</p>'}", element)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
        self.driver.find_element(By.NAME, "repo_upload_file").click()
        self.driver.find_element(By.NAME, "repo_upload_file").send_keys("/Users/nguyenkhanh/Downloads/cryptography-and-network-security_-principles-and-practice-7th-global-edition.pdf")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()