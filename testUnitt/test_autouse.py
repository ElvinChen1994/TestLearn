# -*- coding:utf-8 -*-
# @Time: 2020/3/31 12:12 上午
# @Author: Elvin

'''
平常写自动化用例会写一些前置的fixture操作，用例需要用到就直接传该函数的参数名称就行了。当用例很多的时候，每次都传这个参数，会比较麻烦。
fixture里面有个参数autouse，默认是Fasle没开启的，可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了

调用fixture三种方法

1.函数或类里面方法直接传fixture的函数参数名称
2.使用装饰器@pytest.mark.usefixtures()修饰
3.autouse=True自动使用
'''

import time
import pytest


@pytest.fixture(scope="function")
def start(request):
    print('\n-----开始执行function----')


def test_a(start):
    print("-------用例a执行-------")


class Test_aaa():

    def test_01(self, start):
        print('-----------用例01--------------')

    def test_02(self, start):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_autouse.py"])

'''
使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
'''


@pytest.fixture(scope="function")
def start(request):
    print('\n-----开始执行function----')


@pytest.mark.usefixtures("start")
def test_a():
    print("-------用例a执行-------")


@pytest.mark.usefixtures("start")
class Test_aaa():

    def test_01(self):
        print('-----------用例01--------------')

    def test_02(self):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_autouse.py"])



'''
方法三、autouse设置为True，自动调用fixture功能

start设置scope为module级别，在当前.py用例模块只执行一次，autouse=True自动使用
open_home设置scope为function级别，每个用例前都调用一次，自动使用
'''
import time
import pytest

@pytest.fixture(scope="module", autouse=True)
def start(request):
    print('\n-----开始执行moule----')
    print('module      : %s' % request.module.__name__)
    print('----------启动浏览器---------')
    yield
    print("------------结束测试 end!-----------")

@pytest.fixture(scope="function", autouse=True)
def open_home(request):
    print("function：%s \n--------回到首页--------" % request.function.__name__)

def test_01():
    print('-----------用例01--------------')

def test_02():
    print('-----------用例02------------')

if __name__ == "__main__":
    pytest.main(["-s", "test_autouse.py"])