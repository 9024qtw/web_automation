from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Base(object):
    # driver = webdriver.Edge()
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, loc):
        try:
            ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            return ele
        except Exception as e:
            raise e

    def find_eles(self, loc):
        eles = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
        return eles

    def click_ele(self, loc):
        self.find_ele(loc).click()

    def click_eles(self, loc, num):
        self.find_eles(loc)[num].click()

    def input_text(self, loc, text):
        ele = self.find_ele(loc)
        ele.clear()
        ele.send_keys(text)

    def get_text(self, loc):
        text = self.find_ele(loc).text
        return text
