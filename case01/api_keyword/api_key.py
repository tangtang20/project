import json
import requests
import jsonpath
"""
这是接口关键字驱动类，用于提供接口自动化关键字方法，主要实现常用的关键字内容
"""
class ApiKey:
    # get请求的封装：因为params可能存在无值的情况，存放默认值None
    def send_get(self,url,params=None,**kwargs):
        # 因为请求会返回一个响应，所以函数定义时需要return
        return requests.get(url=url,params=params,**kwargs)
    # post请求的封装：因为data也可能存在无值的情况，也存放默认值None
    def send_post(self,url,data=None,**kwargs):
        return requests.post(url=url,data=data,**kwargs)
    # 基于JosnPath获取数据的关键字，用于提取所有需要的内容
    def get_text(self,txt,key):
        # jsonpath获取数据的表达式:成功则返回list，失败则返回false
        '''
        对于json格式数据的获取，本身是存有目的性来获取的。
        '''
        try:
            #转为json格式数据
            txt=json.loads(txt)
            value=jsonpath.jsonpath(txt,'$..{0}'.format(key))
            if value:
                if len(value)==1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value

if __name__ == '__main__':
    ak = ApiKey()
    data = {
        'username': 'admin',
        'password': '123456'
    }
    res=ak.send_post(url='http://39.98.138.157:5000/api/login', json=data)
    print(res.text)
