import unittest
from POM.page_object.login_page import LoginPage
from POM.page_object.product_page import ProductPage
from selenium import webdriver
import time
from ddt import file_data,ddt
"""
    用例流程：
    1、登录页面
    2、添加购物车
"""
@ddt
class Case01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.lp=LoginPage(cls.driver)
        cls.pg=ProductPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test(self,**kwargs):
        self.lp.login(kwargs['username'],kwargs['password'])
        self.pg.add_cart()
        time.sleep(5)


if __name__=='__main__':
    unittest.main()
