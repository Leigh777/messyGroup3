import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "InvalidUser"
        pwd = "123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath("//*[@id='content']/p").text
            if (elem == 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.'):
                print('Invalid User Error message verified')
                assert True
            else:
                raise AssertionError
        except AssertionError:
            self.fail("Invalid user test failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
