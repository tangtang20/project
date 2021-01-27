"""
    pytest中用例的管理手段：mark
    可以通过mark装饰器对所有的用例进行标记，不同的标记区分进行管理
    -m ：按标记运行测试用例
"""
import pytest

@pytest.mark.webui
@pytest.mark.temp
def test07(zhiyuan2):
    print("测试用例07")


@pytest.mark.interface
@pytest.mark.temp
def test08(zhiyuan2):
    #assert zhiyuan1==2,'异常'
    print("测试用例08")