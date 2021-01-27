import pytest
import requests

from case04.data_driver.yaml_driver import load_yaml

token=None

#传入yaml数据文件
@pytest.mark.parametrize('data',load_yaml('../data/user.yaml'))
def test_login01(data):
    url='http://39.98.138.157:5000/api/login'
    res=requests.post(url=url,json=data)
    #定义全局变量token
    global token
    #从返回的json数据中获取token值
    token=res.json()['token']
    print(token)

#调用预置函数，获取token
def test_login02(get_token):
    print(get_token)
    print(token)



if __name__=='__main__':
    pytest.main(['-sv','test_case02.py'])