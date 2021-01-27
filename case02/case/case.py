import unittest
from ddt import ddt,file_data
from case01.api_keyword.api_key import ApiKey
from case02.config import read_ini

'''
    接口测试的操作执行核心：
        1. 准备数据
        2. 发送请求
        3. 判断响应
'''
@ddt()
class Test_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ak=ApiKey()
        cls.url=read_ini.ReadIni('../config/config','TEST_SERVER','url')
        cls.token=None
        cls.openid=None
        cls.userid=None
        cls.cartid=None
    #login接口的测试用例，yaml文件存放测试数据，一个yaml文件对应一个测试用例
    @file_data('../data/user.yaml')
    def test_01(self,path,data):
        url=self.url+path
        res=self.ak.send_post(url=url,json=data)
        token=self.ak.get_text(res.text,'token')
        if token:
            Test_Case.token=token
        print(res.text)
    #getuserinfo接口测试用例
    @file_data('../data/userinfo.yaml')
    def test_02(self,path,headers):
        url=self.url+path
        headers['token']=self.token
        res=self.ak.send_get(url=url,headers=headers)
        Test_Case.userid=self.ak.get_text(res.text,'userid')
        Test_Case.openid = self.ak.get_text(res.text, 'openid')
        print(res.text)
    #addcart接口测试用例
    @file_data('../data/addcart.yaml')
    def test_03(self,path,headers,data):
        url=self.url+path
        headers['token']=self.token
        data['openid']=self.openid
        data['userid']=self.userid
        res=self.ak.send_post(url=url,headers=headers,json=data)
        Test_Case.cartid=self.ak.get_text(res.text,'cartid')
        print(res.text)
    #createorder接口测试用例
    @file_data('../data/createorder.yaml')
    def test_04(self,path,headers,data):
        url = self.url + path
        headers['token'] = self.token
        data['openid'] = self.openid
        data['userid'] = self.userid
        data['cartid']=self.cartid
        res=self.ak.send_post(url=url,headers=headers,json=data)
        print(res.text)
if __name__=='__main__':
    unittest.main()