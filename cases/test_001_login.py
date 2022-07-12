from page.loginPage import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from common.other import read_yaml_data
from common.mylog import logger

testDatas_01 = read_yaml_data("/datas/userdata.yaml")
print(testDatas_01)


class TestLogin:
    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://localhost:80/redmine')
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        logger.info("测试套件执行前".format(__name__))

    def teardown(self):
        self.driver.quit()
        logger.info("测试套件执行后".format(__name__))

    @pytest.mark.parametrize("name, pwd", [(testDatas_01['userInfo'][0]['name'], testDatas_01['userInfo'][0]['pwd'])])
    @pytest.mark.L1
    def test_login_suc(self, name, pwd):
        self.lp.enter_login()
        self.lp.input_user(user=name)
        self.lp.input_pwd(pwd=pwd)
        self.lp.click_login()
        with allure.step('截图'):
            allure.attach(self.driver.get_screenshot_as_png(), '登录成功', allure.attachment_type.PNG)
        logger.info(f"用户{testDatas_01['userInfo'][0]['name']}登录成功")
        assert self.lp.get_text((By.LINK_TEXT, 'admin')) == 'admin'

    @pytest.mark.parametrize("name, pwd", [(testDatas_01['userInfo'][1]['name'], testDatas_01['userInfo'][1]['pwd'])])
    @pytest.mark.L1
    def test_login_fail(self, name, pwd):
        self.lp.enter_login()
        self.lp.input_user(user=name)
        self.lp.input_pwd(pwd=pwd)
        self.lp.click_login()
        with allure.step('截图'):
            allure.attach(self.driver.get_screenshot_as_png(), '登录失败', allure.attachment_type.PNG)
        logger.info(f"用户{testDatas_01['userInfo'][0]['name']}登录失败")
        assert self.lp.get_text((By.ID, 'flash_error')) == '无效的用户名或密码'
