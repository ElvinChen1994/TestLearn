# -*- coding:utf-8 -*-
# @Time: 2020/3/30 10:48 下午
# @Author: Elvin
'''
pytest可以支持自定义标记，自定义标记可以把一个web项目划分多个模块，然后指定模块名称执行。app自动化的时候，如果想android和ios公用一套代码时，
也可以使用标记功能，标明哪些是ios用例，哪些是android的，运行代码时候指定mark名称运行就可以
'''

import pytest

@pytest.mark.webtest
def test_send_http():
    pass

def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass

if __name__ == '__main__':
    pytest.main(["-s", "test_mark.py", "-m=webtest"])

'''
只运行用webtest标记的测试，cmd运行的时候，加个-m 参数，指定参数值webtest
'''
'''
如果不想执行标记webtest的用例，那就用”not webtest”
'''
@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app
def test_something_quick():
    pass
def test_another():
    pass
class TestClass:
    def test_method(self):
        pass

if __name__ == "__main__":
    pytest.main(["-s", "test_server.py", "-m='not webtest'"])

''''
如果想指定运行某个.py模块下，类里面的一个用例，如：TestClass里面testmethod用例
每个test开头(或_test结尾)的用例，函数(或方法)的名称就是用例的节点id，指定节点id运行用-v 参数
'''

if __name__ == "__main__":
    pytest.main(["-v", "test_server.py::TestClass::test_method"])


'''
可以使用-k命令行选项指定在匹配用例名称的表达式

$ pytest -v -k http

您也可以运行所有的测试，根据用例名称排除掉某些用例：

$ pytest -k “not send_http” -v

您也可以运行所有的测试，根据用例名称排除掉某些用例：

$ pytest -k “not send_http” -v


'''



import pytest

@pytest.mark.webtest
def test_send_http():
    print("mark web test")

def test_something_quick():
    pass

def test_another():
    pass

@pytest.mark.hello
class TestClass:
    def test_01(self):
        print("hello :")

    def test_02(self):
        print("hello world!")

if __name__ == "__main__":
    pytest.main(["-v", "test_mark.py", "-m=hello"])