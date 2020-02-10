from getgauge.python import before_suite, after_suite
from selenium import webdriver

class Driver(object):
    # driver = None
    driver = None
    @before_suite
    def init():
        Driver.driver = webdriver.Chrome('C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe')

    @after_suite
    def close():
        Driver.driver.close()