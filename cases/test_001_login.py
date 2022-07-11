from page.loginPage import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


class TestLogin:
    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://localhost:80/redmine')
        self.driver.maximize_window()
        self.lp = Login(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.L1
    def test_login_suc(self):
        self.lp.enter_login()
        self.lp.input_user(user='admin')
        self.lp.input_pwd(pwd='11111111')
        self.lp.click_login()
        with allure.step('截图'):
            allure.attach(self.driver.get_screenshot_as_png(), '登录成功', allure.attachment_type.PNG)
        assert self.lp.get_text((By.LINK_TEXT, 'admin')) == 'admin'

    @pytest.mark.L1
    def test_login_fail(self):
        self.lp.enter_login()
        self.lp.input_user(user='admin')
        self.lp.input_pwd(pwd='12345678')
        self.lp.click_login()
        with allure.step('截图'):
            allure.attach(self.driver.get_screenshot_as_png(), '登录失败', allure.attachment_type.PNG)
        assert self.lp.get_text((By.ID, 'flash_error')) == '无效的用户名或密码'



