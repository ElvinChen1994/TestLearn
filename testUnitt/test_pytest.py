# -*- coding:utf-8 -*-
# @Time: 2020/3/13 2:45 下午
# @Author: Elvin

import pytest

def inc(x):
    return x + 1


def test_answer(x):
    assert inc(x) == 5


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    @pytest.mark.skip(reason="跳过")
    def test_one(self):
        assert True

    @pytest.mark.skipif(True, reason="跳过")
    def test_two(self):
        assert False

    def test_three(self):
        assert True