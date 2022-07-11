from page.loginPage import Login
from page.new_bug_page import NewBugPage
from page.projectPage import ProjectDetailsPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


class TestNewBug:

    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('http://localhost:80/redmine')
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.login(user_name='admin', password='11111111')
        self.pd = ProjectDetailsPage(self.driver)
        self.nb = NewBugPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.L1
    def test_new_bug(self):
        self.pd.enter_project()
        self.pd.choose_project()
        self.nb.enter_bug()
        self.nb.create_new_bug()
        self.nb.input_bug_name(bn='登录407')
        self.nb.click_create()
        allure.attach(self.driver.get_screenshot_as_png(), '新建bug成功', allure.attachment_type.PNG)
        text = self.nb.get_text((By.XPATH, '//*[@id="flash_notice"]/a'))
        info = '问题 ' + text + ' 已创建。'
        print(info)
        assert self.nb.get_text((By.XPATH, '//div[@id="flash_notice"]')) == info


