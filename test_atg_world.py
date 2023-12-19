# test_atg_world.py
import unittest
from selenium import webdriver

class TestATGWorld(unittest.TestCase):
    def test_website_loading(self):
        driver = webdriver.Chrome()  # Use appropriate driver
        driver.get("https://atg.world")
        self.assertEqual(driver.title, "ATG World")  # Adjust based on the actual title
        driver.quit()

if __name__ == "__main__":
    unittest.main()
