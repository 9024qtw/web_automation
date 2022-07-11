from common.base import Base
from selenium.webdriver.common.by import By


# 项目页面
class ProjectMainPage(Base):

    # 进入项目页面
    def enter_project(self):
        self.click_ele((By.LINK_TEXT, '项目'))

    # 创建新项目
    def create_new_project(self):
        self.click_ele((By.LINK_TEXT, '新建项目'))


# 创建新项目页面
class NewProjectPage(ProjectMainPage):

    # 输入项目名称
    def input_project_name(self, name):
        self.input_text((By.ID, 'project_name'), text=name)

    # 创建
    def create(self):
        self.click_ele((By.NAME, 'commit'))


class ProjectDetailsPage(NewProjectPage):

    def choose_project(self):
        self.click_ele((By.XPATH, '//*[@id="projects-index"]/ul/li[1]/div/a'))

