import unittest,requests
from ddt import ddt,file_data
from case01.api_keyword.api_key import ApiKey

@ddt()
class ApiCaes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ak=ApiKey()
    @file_data('../user.yaml')
    def test01(self,user,msg):
        url='http://39.98.138.157:5000/api/login'
        data={
            'username':user['username'],
            'password':user['password']
        }
        res=self.ak.send_post(url=url,json=data)
        print(res.text)
        #获取响应的结果，校验是否成功
        value=self.ak.get_text(res.text,'msg')
        #print(value)
        self.assertEqual(value,msg,msg='异常')
if __name__ == '__main__':
    unittest.main()