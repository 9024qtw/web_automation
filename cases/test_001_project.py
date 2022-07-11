from page.loginPage import Login
from page.projectPage import NewProjectPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


class TestCreatPrject:
    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://localhost:80/redmine')
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.login(user_name='admin', password='11111111')
        self.cp = NewProjectPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.L2
    def test_create_project_suc(self):
        project_name = 'project' + str(time.time())
        self.cp.enter_project()
        self.cp.create_new_project()
        self.cp.input_project_name(name=project_name)
        self.cp.create()
        allure.attach(self.driver.get_screenshot_as_png(), '创建项目成功', attachment_type=allure.attachment_type.PNG)
        assert self.cp.get_text((By.ID, 'flash_notice')) == '创建成功'

