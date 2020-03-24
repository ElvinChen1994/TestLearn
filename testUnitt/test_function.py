# -*- coding:utf-8 -*-
# @Time: 2020/3/24 9:06 下午
# @Author: Elvin
#模块级（setup_module/teardown_module）开始于模块始末，全局的
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
# # 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
# # 方法级（setup_method/teardown_method）开始于方法始末（在类中）
# # 类里面的（setup/teardown）运行在调用方法的前后


'''
setup_module是所有用例开始前只执行一次，teardown_module是所有用例结束后只执行一次
'''
import pytest
import sys

def setup_function():
    print("setup_function: 每个用例开始前都会执行")

def teardown_function():
    print("teardown_function: 每个用例结束后都会执行")

def test_one():
    print("正在执行------test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行-------test_two")
    x = "hello"
    assert hasattr(test_two(), "hello")
    sys.setrecursionlimit(1)
def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

if __name__ == "__main__":

    pytest.main(["-s", "test_function.py"])


'''
类和方法
'''
import pytest

class TestCase():

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class: 所有用例执行之前")

    def teardown_method(self):
        print("teardown_method: 每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        a = "hello"
        b = "hello world"
        assert a in b

if __name__ == "__main__":
    pytest.main(["-s", "test_function.py"])

'''
函数和类混合
'''
def setup_module():
    print("setup_module: 整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module: 整个.py模块执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function: 每个用例开始前都会执行")

def test_one():
    print("正在执行-----test_one")
    x = "this"
    assert 'h' in x
class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])