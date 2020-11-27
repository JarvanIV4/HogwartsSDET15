# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/11/26 22:27
import pytest


@pytest.fixture(autouse=True)
def login():
    print("登录用例")
    yield ['tom', '123456']
    print("登出用例")


@pytest.mark.usefixtures("login")
def test_login2():
    print("登录用例2")


def test_search1():
    print("搜索用例")


def test_search2(login):
    print("搜索用例2")
