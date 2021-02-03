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
    #关联赋值行为
    def assignment(self,kwargs):
        #dict.items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
        for key,value in kwargs.items():
            #基于数据的内容的格式来判断基于何种处理方式
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key]=getattr(self,key)
        return kwargs

    @classmethod
    def setUpClass(cls):
        cls.ak=ApiKey()
        cls.url=read_ini.ReadIni('config','TEST_SERVER','url')
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
    def test_03(self,path,**kwargs):
        url=self.url+path
        # headers['token']=self.token
        # data['openid']=self.openid
        # data['userid']=self.userid
        value = self.assignment(kwargs)
        print(value)
        res=self.ak.send_post(url=url,headers=value['headers'],json=value['data'])
        Test_Case.cartid=self.ak.get_text(res.text,'cartid')
        print(res.text)
    #createorder接口测试用例
    @file_data('../data/createorder.yaml')
    def test_04(self,path,**kwargs):
        url = self.url + path
        # headers['token'] = self.token
        # data['openid'] = self.openid
        # data['userid'] = self.userid
        # data['cartid']=self.cartid
        value=self.assignment(kwargs)
        print(value)
        res=self.ak.send_post(url=url,headers=value['headers'],json=value['data'])
        print(res.text)
if __name__=='__main__':
    unittest.main()