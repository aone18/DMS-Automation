from selenium import webdriver
import pytest
from utils import insert,click
email_key = "admin@gentech.com"
password_key = "admin123"
from pages.role import role

class TestLogin:
    def setup_method(self):
        # Create new instance of the Chrome Driver
        self.driver = webdriver.Chrome()
    def test_login(self):
         # navigate to login page
         self.driver.get("http://localhost:3000/#/login")
         insert(self.driver, "//*[@id='signin-form']/div[1]/input", email_key)
         insert(self.driver, "//*[@id='signin-form']/div[2]/input", password_key)

         click(self.driver, "//*[@id='signin-form']/div[3]/div/button")
         assert self.driver.title == "General DMS"

        # role(self.driver)





