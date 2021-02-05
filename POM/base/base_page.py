"""
    基类：提供给所有页面对象的基本调用的工具类
"""
from selenium import webdriver
from time import sleep

class BasePage:
    # driver=webdriver.Chrome()
    url='http://39.98.138.157/shopxo/index.php'
    #定义构造函数
    def __init__(self,driver):
        self.driver=driver

    #定义页面访问
    def visit(self,url):
        self.driver.get(url)

    #定义退出浏览器
    def quit(self):
        self.driver.quit()

    #定义元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    #定义输入信息
    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    #定义点击
    def click(self,loc):
        self.locator(loc).click()

    #定义隐式等待
    def wait(self,time):
        self.driver.implicitly_wait(time)

    #定义强制等待
    def sleep(self,time):
        sleep(time)

