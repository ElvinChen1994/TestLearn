# -*- coding:utf-8 -*-
# @Time: 2020/3/31 1:16 上午
# @Author: Elvin
import pytest



'''
如果想把登录操作放到前置操作里，也就是用到@pytest.fixture装饰器，传参就用默认的request参数
user = request.param 这一步是接收传入的参数，本案例是传一个参数情况
添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数
'''

#测试账号数据
test_user_data = ["admin1", "admin2"]
@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户: %s" % user)
    return user

@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print("测试用例中login的返回值: %s" % a)
    assert a != " "

if __name__ == '__main__':
    pytest.main(["-s", "test_request.py"])


'''
添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数
'''
# 测试账号数据
test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin1", "psw": ""}]

@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return True
    else:
        return False

# indirect=True 声明login是个函数
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a, "失败原因：密码为空"

if __name__ == "__main__":
    pytest.main(["-s", "test_request.py"])
'''
如果要用到login里面的返回值，def test_login(login)时，传入login参数，函数返回值就是login了
'''

'''
用例上面是可以同时放多个fixture的，也就是多个前置操作，可以支持装饰器叠加，使用parametrize装饰器叠加时，用例组合是2个参数个数相乘
'''

import pytest

# 测试账号数据
test_user = ["admin1", "admin2"]
test_psw = ["11111", "22222"]

@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw

@pytest.mark.parametrize("input_user", test_user, indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user, input_psw):
    '''登录用例'''
    a = input_user
    b = input_psw
    print("测试数据a-> %s， b-> %s" % (a,b))
    assert b

if __name__ == "__main__":
    pytest.main(["-s", "test_04.py"])

'''
如果参数user有2个数据，参数psw有2个数据，那么组合起来的案例是两个相乘，也就是组合2*2 = 4个用例
'''