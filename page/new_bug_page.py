from common.base import Base
from selenium.webdriver.common.by import By


class NewBugPage(Base):
    def enter_bug(self):
        self.click_ele((By.LINK_TEXT, '问题'))

    def create_new_bug(self):
        self.click_ele((By.LINK_TEXT, '新建问题'))

    def input_bug_name(self, bn):
        self.input_text((By.ID, 'issue_subject'), text=bn)

    def click_create(self):
        self.click_ele((By.NAME, 'commit'))


