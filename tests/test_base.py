import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com")

    def tearDown(self):
        self.driver.quit()
