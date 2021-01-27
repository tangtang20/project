'''
这是pytest中的预置函数定义的配置文件：注意，文件名称一定是conftest。不能是其他的
scope参数定义的4种等级（默认等级是function）：
    session：在本次session级别中只执行一次
    module：在模块级别中只执行一次
    class：在类级别中只执行一次
    function：在函数级别中执行，每有一个函数就执行一次
'''

import pytest


#预置函数，用于前期数据的准备
#例如接口关联，每次都要用到token,我们就可以放到预制函数，获取token，某个用例要调用的时候
#把预制函数作为参数传到用例中，在运行用例前先获取token
@pytest.fixture(scope='session')
def zhiyuan1():
    return 1

@pytest.fixture(scope='session')
def zhiyuan2():
    print('志远很强')