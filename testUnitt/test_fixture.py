# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:34 下午
# @Author: Elvin


'''
命名方式灵活，不局限于setup和teardown这几个命名
conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
scope=”module” 可以实现多个.py跨文件共享前置
scope=”session” 以实现多个.py跨文件使用一个session来完成多个用例

Fixtures可以选择使用yield语句为测试函数提供它们的值，而不是return。 在这种情况下，yield语句之后的代码块作为拆卸代码执行，而不管测试结果如何。fixture功能必须只产生一次
可以使用此装饰器（带或不带参数）来定义fixture功能。 fixture功能的名称可以在以后使用
 引用它会在运行测试之前调用它：test模块或类可以使用pytest.mark.usefixtures（fixturename标记。
 测试功能可以直接使用fixture名称作为输入参数，在这种情况下，夹具实例从fixture返回功能将被注入。

:arg scope: scope 有四个级别参数 "function" (默认), "class", "module" or "session".

:arg params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它

:arg autouse:  如果为True，则为所有测试激活fixture func 可以看到它。 如果为False（默认值）则显式需要参考来激活fixture

:arg ids: 每个字符串id的列表，每个字符串对应于params 这样他们就是测试ID的一部分。 如果没有提供ID它们将从params自动生成

:arg name:   fixture的名称。 这默认为装饰函数的名称。 如果fixture在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽; 解决这个问题的一种方法是将装饰函数命名
                   “fixture_ <fixturename>”然后使用”@ pytest.fixture（name ='<fixturename>'）“”。
'''


import pytest

# 不带参数时默认scope="function"
@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fix.py"])


'''
conftest.py配置需要注意以下点：
conftest.py配置脚本名称是固定的，不能改名称
conftest.py与运行的用例要在同一个pakage下，并且有init.py文件
不需要import导入 conftest.py，pytest用例会自动查找

'''
__init__.py

conftest.py
    # coding:utf-8
    import pytest

    @pytest.fixture()
    def login():
        print("输入账号，密码先登录")

test_fix1.py
    # coding:utf-8
    import pytest

    def test_s1(login):
        print("用例1：登录之后其它动作111")

    def test_s2():  # 不传login
        print("用例2：不需要登录，操作222")

    def test_s3(login):
        print("用例3：登录之后其它动作333")

    if __name__ == "__main__":
        pytest.main(["-s", "test_fix1.py"])

test_fix2.py
    # coding:utf-8
    import pytest

    def test_s4(login):
        print("用例4：登录之后其它动作111")

    def test_s5():  # 不传login
        print("用例5：不需要登录，操作222")

    if __name__ == "__main__":
        pytest.main(["-s", "test_fix2.py"])


'''
这里用到fixture的teardown操作并不是独立的函数，用yield关键字呼唤teardown操作
'''
import pytest
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):  # 不传login
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])

'''
既然有setup那就有teardown,fixture里面的teardown用yield来唤醒teardown的执行
'''
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

    yield
    print("执行teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):  # 不传login
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])

'''
如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，并且在用例全部执行完之后，会呼唤teardown的内容
'''
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError  # 模拟异常

def test_s2(open):  # 不传login
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])

'''
除了yield可以实现teardown,在request-context对象中注册addfinalizer方法也可以实现终结函数
'''
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()
    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value

'''
yield和addfinalizer方法都是在测试完成后呼叫相应的代码。但是addfinalizer不同的是：

他可以注册多个终结函数。
这些终结方法总是会被执行，无论在之前的setup code有没有抛出错误。这个方法对于正确关闭所有的fixture创建的资源非常便利，即使其一在创建或获取时失败
'''