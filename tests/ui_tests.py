import unittest
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestUserInterfaceClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        dir = os.path.dirname(os.path.abspath(__file__))
        cls.driver = webdriver.Chrome(executable_path=dir + '/chromedriver')
        # navigate to the application home page
        cls.driver.get("http://www.google.com/")
        cls.driver.title

    def setUp(self):
        try:
            dir = os.path.dirname(os.path.abspath(__file__))
            self.driver = webdriver.Chrome(executable_path=dir + '/chromedriver')
        except Exception as issue:
            logging.warning('Could not start Chrome Webdriver. Is chromedriver.exe in the test directory?\n Caught Exception: %s', issue)
        self.options = webdriver.ChromeOptions()
        self.options.add('--disable-gpu')
        self.options.add('--headless')

        try:
            logging.info('Connecting to ')
            self.driver.get('http://127.0.0.1:5000')
        except Exception as issue:
            logging.warning('Could not connect to UI. Did you start the app? \n Caught Exception: %s', issue)
            exit(1)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def test_login_page(self):
        pass


    """
    Homepage Test
    
    - Check that "Username" string exists
    - Check that "Password" string exists
    - Check that Two Inputs exists
    - Check that login button exists
    """


    """
    Assessment Test
    
    - Check that there is "Assessment" button
    - Try to input a symptom
    - Check response
    -  
    """



if __name__ == '__main__':
    unittest.main()
