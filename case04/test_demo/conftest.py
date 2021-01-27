import pytest
import requests

#预置函数，获取token，可以多模块间调用g

@pytest.fixture()
def get_token():
    url='http://39.98.138.157:5000/api/login'
    data={
        'username':'admin',
        'password':'123456'
    }
    res=requests.post(url=url,json=data)
    token=res.json()['token']
    return token

#print(get_token())