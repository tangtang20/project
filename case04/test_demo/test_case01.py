import pytest
from case04.data_driver.yaml_driver import load_yaml

"""
pytest.mark.parametrize(): pytest数据驱动实现方式，类似ddt于unittest
allure报告生成：
1、生成result命令：pytest -s --alluredir ../result/
2、生成allure报告命令：allure generate ../result/ -o ../report_allure/    
   --clear :生成新的报告并清除原来的
"""

@pytest.mark.parametrize(['user','password'],[('admin','123456'),('admin1','')])
def test_login(user,password):
    print('---------')
    print(user)
    print(password)

#传入yaml数据
@pytest.mark.parametrize('data',load_yaml('../data/user.yaml'))
def test_login1(data):
    print(data)
    print(data['user'])
    print(data['password'])


if __name__=='__main__':
    pytest.main(['-sv'])