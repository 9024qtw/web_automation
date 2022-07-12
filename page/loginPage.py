from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.other import read_yaml_data

element_datas = read_yaml_data(yaml_path='/datas/element.yaml')
login_datas = element_datas['LoginPage']


class Login(Base):

    def enter_login(self):
        self.click_ele((login_datas[0]['type'], login_datas[0]['value']))

    def input_user(self, user):
        self.input_text((login_datas[1]['type'], login_datas[1]['value']), text=user)

    def input_pwd(self, pwd):
        self.input_text((login_datas[2]['type'], login_datas[2]['value']), text=pwd)

    def click_login(self):
        self.click_ele((login_datas[3]['type'], login_datas[3]['value']))

    def login(self, user_name, password):
        self.enter_login()
        self.input_user(user=user_name)
        self.input_pwd(pwd=password)
        self.click_login()


if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get('http://localhost:80/redmine/')
    driver.maximize_window()
    lp = Login(driver)
    lp.login(user_name='admin', password='11111111')
    driver.quit()
