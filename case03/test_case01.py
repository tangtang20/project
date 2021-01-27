import pytest
'''
    Pytest默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
    Pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
    多条指令一同运行时，需要通过空格进行区分，在main函数中，是通过,进行分割
    -v 用于详细显示日志信息
    -rA 测试结果的简单统计
    -q 忽略
    pytest中的setup和teardown：一般可以通过一个配置文件直接进行管理：配置文件命名一定要是conftest.py
    pytest.ini是pytest核心配置文件，最好放在根目录下，可以控制全局
    pytest生成测试报告：pytest_html测试报告模块
    运行命令：pytest --html=./report/report.html,如果要集成到邮件，就需要添加指令--self-contained-html
'''
#前置后置条件
def setup_function():
    print('Sfunction')

def teardown_function():
    print('tfuction')

def setup_module():
    print('smodule')

def teardown_module():
    print('tmodule')

#测试用例
def test01():
    print("测试用例01")

def test02():
    print("测试用例02")

# pytest中class对象的定义：建议以test开头
'''
    在class中前置后置函数的运行顺序：
        setup class
        setup method
        setup
        teardown
        teardown method
        teardown class
'''

class CaseDemo:
    def setup(self):
        print('第三前置函数')

    def teardown(self):
        print('第三后置函数')

    def setup_class(self):
        print('第一前置函数')

    def teardown_class(self):
        print('第一后置函数')

    def setup_method(self):
        print('第二前置函数')

    def teardown_method(self):
        print('第二后置函数')

    def test03(self):
        print("测试用例03")

    def test04(self):
        print("测试用例04")

if __name__=='__main__':
    pytest.main()