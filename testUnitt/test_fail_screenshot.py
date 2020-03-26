# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:50 下午
# @Author: Elvin
from selenium import webdriver
import pytest

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():

    return driver.get_screenshot_as_base64()

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Firefox()
    return driver

'''
用例
'''
from selenium import webdriver
import time


def test_yoyo_01(browser:webdriver.Firefox):

    browser.get("https://www.cnblogs.com/")
    time.sleep(2)
    t = browser.title
    assert t == ""

# test_02.py文件

from selenium import webdriver
import time


def test_yoyo_01(browser:webdriver.Firefox):

    browser.get("https://www.cnblogs.com/")
    time.sleep(2)
    t = browser.title
    assert "" in t

'''
$ pytest —html=report.html —self-contained-html
$ py.test —rerun 1  —html=report.html —self-contained-html
'''