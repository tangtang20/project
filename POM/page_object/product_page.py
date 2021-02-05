from POM.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

#添加购物车页面对象
class ProductPage(BasePage):
    url=BasePage.url+'?s=/index/goods/index/id/2.html'
    #页面关联元素
    suite=(By.XPATH,'//li[@data-value="套餐一"]')
    color=(By.XPATH,'//li[@data-value="金色"]')
    memory=(By.XPATH,'//li[@data-value="32G"]')
    addcart=(By.XPATH,'//button[@title="加入购物车"]')
    #添加购物车操作行为
    def add_cart(self):
        self.wait(10)
        self.visit(url=self.url)
        self.click(self.suite)
        self.click(self.color)
        self.click(self.memory)
        self.click(self.addcart)

if __name__=='__main__':
    driver=webdriver.Chrome()
    pg=ProductPage(driver)
    pg.add_cart()

