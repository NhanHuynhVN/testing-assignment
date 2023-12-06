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
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
       
        settingBtn = self.driver.find_element(By.CSS_SELECTOR,'li[data-key="editsettings"]')
        settingBtn.click()
        time.sleep(1)

        full_site_name = self.driver.find_element(By.XPATH,'//*[@id="id_s__fullname"]')
        full_site_name.clear()
        full_site_name.send_keys("Site A")
        time.sleep(1)

        short_site_name = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[3]/div[2]/div[1]/input')
        short_site_name.clear()
        short_site_name.send_keys("sitA")
        time.sleep(1)

        maximum_num_of_courses = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[8]/div[2]/div[1]/input')
        maximum_num_of_courses.clear()
        maximum_num_of_courses.send_keys(10)
        time.sleep(1)

        comment_displayed_per_page = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[11]/div[2]/div[1]/input')
        comment_displayed_per_page.clear()
        comment_displayed_per_page.send_keys(10)
        time.sleep(1)
        

        saveBtn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/div/div/button')
        saveBtn.click()
        time.sleep(1)
        
        alert = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/span/div')
        assert alert != None

    def test_2(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
       
        settingBtn = self.driver.find_element(By.CSS_SELECTOR,'li[data-key="editsettings"]')
        settingBtn.click()
        time.sleep(1)

        full_site_name = self.driver.find_element(By.XPATH,'//*[@id="id_s__fullname"]')
        full_site_name.clear()
        time.sleep(1)

        short_site_name = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[3]/div[2]/div[1]/input')
        short_site_name.clear()
        short_site_name.send_keys("sitA")
        time.sleep(1)

        maximum_num_of_courses = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[8]/div[2]/div[1]/input')
        maximum_num_of_courses.clear()
        maximum_num_of_courses.send_keys(10)
        time.sleep(1)

        comment_displayed_per_page = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[11]/div[2]/div[1]/input')
        comment_displayed_per_page.clear()
        comment_displayed_per_page.send_keys(10)
        time.sleep(1)
        

        saveBtn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/div/div/button')
        saveBtn.click()
        time.sleep(1)
        
        alert = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div') 
        assert alert != None


    def test_3(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
       
        settingBtn = self.driver.find_element(By.CSS_SELECTOR,'li[data-key="editsettings"]')
        settingBtn.click()
        time.sleep(1)

        full_site_name = self.driver.find_element(By.XPATH,'//*[@id="id_s__fullname"]')
        full_site_name.clear()
        full_site_name.send_keys("Site A")
        time.sleep(1)

        short_site_name = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[3]/div[2]/div[1]/input')
        short_site_name.clear()
        time.sleep(1)

        maximum_num_of_courses = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[8]/div[2]/div[1]/input')
        maximum_num_of_courses.clear()
        maximum_num_of_courses.send_keys(10)
        time.sleep(1)

        comment_displayed_per_page = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[11]/div[2]/div[1]/input')
        comment_displayed_per_page.clear()
        comment_displayed_per_page.send_keys(10)
        time.sleep(1)
        

        saveBtn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/div/div/button')
        saveBtn.click()
        time.sleep(1)
        
        alert = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div')
        assert alert != None

    def test_4(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
       
        settingBtn = self.driver.find_element(By.CSS_SELECTOR,'li[data-key="editsettings"]')
        settingBtn.click()
        time.sleep(1)

        full_site_name = self.driver.find_element(By.XPATH,'//*[@id="id_s__fullname"]')
        full_site_name.clear()
        full_site_name.send_keys("Site A")
        time.sleep(1)

        short_site_name = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[3]/div[2]/div[1]/input')
        short_site_name.clear()
        short_site_name.send_keys("sitA")
        time.sleep(1)

        maximum_num_of_courses = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[8]/div[2]/div[1]/input')
        maximum_num_of_courses.clear()
        maximum_num_of_courses.send_keys(-1)
        time.sleep(1)

        comment_displayed_per_page = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[11]/div[2]/div[1]/input')
        comment_displayed_per_page.clear()
        comment_displayed_per_page.send_keys(10)
        time.sleep(1)
        

        saveBtn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/div/div/button')
        saveBtn.click()
        time.sleep(1)
        
        try: 
            alert = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div')
            assert alert != None
        except:
            assert False

    def test_5(self): #done
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.ID,"loginbtn")
        username.send_keys("admin")
        password.send_keys("sandbox")
        submitBtn.click()
        time.sleep(2)
       
        settingBtn = self.driver.find_element(By.CSS_SELECTOR,'li[data-key="editsettings"]')
        settingBtn.click()
        time.sleep(1)

        full_site_name = self.driver.find_element(By.XPATH,'//*[@id="id_s__fullname"]')
        full_site_name.clear()
        full_site_name.send_keys("Site A")
        time.sleep(1)

        short_site_name = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[3]/div[2]/div[1]/input')
        short_site_name.clear()
        short_site_name.send_keys("sitA")
        time.sleep(1)

        maximum_num_of_courses = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[8]/div[2]/div[1]/input')
        maximum_num_of_courses.clear()
        maximum_num_of_courses.send_keys(10)
        time.sleep(1)

        comment_displayed_per_page = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/fieldset/div[11]/div[2]/div[1]/input')
        comment_displayed_per_page.clear()
        comment_displayed_per_page.send_keys(-1)
        time.sleep(1)
        

        saveBtn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/form/div/div/div/button')
        saveBtn.click()
        time.sleep(1)
        
        try: 
            alert = self.driver.find_element(By.XPATH,'//*[@id="region-main"]/div/div')
            assert alert != None
        except:
            assert False

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()