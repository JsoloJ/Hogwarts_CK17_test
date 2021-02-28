#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import datetime

@pytest.fixture()
def login():
    print("登录操作")
    a = datetime.datetime.now()
    yield a
    print("登出操作")

#使用fixture调用fixture
@pytest.fixture()
def get_username(login):
    name = "赫敏"
    print(name)
    yield name
    print("名字二")

def test_search(get_username,login):
    print("搜索")
    print(login)
    print(get_username)



@pytest.mark.usefixtures("login")
def test_cart():
    print("购物")


@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("下单")


