# -*- coding:utf-8 -*-
# @Time: 2020/3/24 3:07 上午
# @Author: Elvin

'''
@allure.epic() epic描述 敏捷里面定义史诗，往下是fetature
@allure.feature() 模块名称 功能点描述，往下是story
@allure.story() 用户故事 用户故事往下是title
@allure.title(用例的标题) 用例标题 重命名html名称
@allure.testcase()测试用例的链接地址，对应功能测试用例系统里面的case
@allure.issure() 缺陷 对应缺陷管理系统里面的链接
@allure.description 用例描述 测试用例的描述
@allure.step() 操作步骤 测试用例步骤
@allure.severity() 用例等级 blocker, critical, normal, minor, trivial
@allure.link() 链接 定义一个链接，在测试报告展现
@allure.attachment() 附件 报告添加附件
'''

import pytest
import allure

@pytest.fixture(scope="session")
def login_fixure():
    print("前置条件：登录")

@allure.step("步骤1")
def step_1():
    print("操作步骤--------------------1")

@allure.step("步骤2")
def step_2():
    print("操作步骤--------------------2")

@allure.step("步骤3")
def step_3():
    print("操作步骤--------------------3")

@allure.epic("")

@allure.epic("epic对大Story的一个描述性标签")
@allure.feature("测试模块")
class TestDemoAllure():

    @allure.testcase("http://49.235.x.x:8080/zentao/testcase-view-6-1.html")
    @allure.issue("http://49.235.x.x:8080/zentao/bug-view-1.html")
    @allure.title("用例的标题")
    @allure.story("用户故事：1")
    @allure.severity("critical")
    def test_case_1(self, login_fixture):
        '''case description:
        1.点文章分类导航标签 -跳转编辑页面
        2.编辑页面输入，分类名称，
        3.点保存按钮保存成功
        '''
        step_1()
        step_2()

    @allure.story("用户故事：2")
    def test_case_2(self, login_fixture):
        print("测试用例1")
        step_1()
        step_3()

@allure.epic("epic对大Story的一个描述性标签")
@allure.feature("模块2")
class TestDemo2():

    @allure.story("用户故事：3")
    def test_case_3(self, login_fixture):
        print("测试用例1")
        step_1()

    @allure.story("用户故事：4")
    def test_case_4(self, login_fixture):
        print("测试用例1")
        step_3()
