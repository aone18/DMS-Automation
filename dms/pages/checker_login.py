from utils import click, insert

email_key = "sagar@rbb.com.np"
password_key = "Aone@1234"


def checker_login(driver):
    insert(driver, "//*[@id='signin-form']/div[1]/input", email_key)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password_key)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")