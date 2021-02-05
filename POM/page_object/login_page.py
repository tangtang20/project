'''
    LoginPage：实现登录页面对象的封装，以便于流程需要时进行调用
'''
from selenium import webdriver
from POM.base.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    #页面url：每一个不同的页面对象对应的都是不同的页面，就会有不同的url
    url=BasePage.url+'?s=/index/user/logininfo.html'
    #页面元素
    user=(By.NAME,'accounts')
    pwd=(By.NAME,'pwd')
    button=(By.XPATH,"//button[text()='登录']")
    #页面登录操作行为
    def login(self,username,password):
        self.visit(self.url)
        self.input(self.user,username)
        self.input(self.pwd,password)
        self.click(self.button)

if __name__=='__main__':
    diver=webdriver.Chrome()
    lp=LoginPage(diver)
    lp.login('xuzhu666','123456')
    sleep(5)
    lp.quit()
