# test_atg_website.py

import unittest
from selenium import webdriver

class TestATGWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # or use the appropriate webdriver for your browser
        self.base_url = "https://atg.world"

    def test_website_loading(self):
        self.driver.get(self.base_url)
        self.assertTrue("ATG" in self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

