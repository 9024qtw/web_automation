from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


class Login(Base):

    def enter_login(self):
        self.click_ele((By.LINK_TEXT, '登录'))

    def input_user(self, user):
        self.input_text((By.ID, 'username'), text=user)

    def input_pwd(self, pwd):
        self.input_text((By.ID, 'password'), text=pwd)

    def click_login(self):
        self.click_ele((By.ID, 'login-submit'))

    def login(self, user_name, password):
        self.enter_login()
        self.input_user(user=user_name)
        self.input_pwd(pwd=password)
        self.click_login()


if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get('http://localhost:80/redmine')
    driver.maximize_window()
    lp = Login(driver)
    lp.login()
    lp.input_user()
    lp.input_pwd()
    lp.click_login()
    assert driver.find_element(By.LINK_TEXT, 'admin').text == 'admin'
