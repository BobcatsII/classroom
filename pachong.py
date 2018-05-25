#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/5/8 16:09
# @Author : linan
# @File   : pachong.py

import requests
from lxml import html

login_url = "http://1xxxxx:85/arsys/shared/login.jsp"
session_url = "http://11xxxxxx:55/arsys/servlet/LoginServlet"

s = requests.session()
r = s.get(login_url)
tree = html.fromstring(r.text)
el = tree.xpath('//input[@name="encpwd"]')[0]
encpwd = el.attrib["value"]

data = {
    "username": "xxxx",
    "pwd": "xxx",
    "auth":"",
    "timezone": "Antarctica/Casey",
    "encpwd": encpwd,
    "goto":"",
    "server":"",
    "ipoverride": 0,
    "initialState": 0,
    "returnBack": "/arsys/home"
}

t = s.post(session_url, data=data)
print (t.url)

el = tree.xpath('//div[@class="BaseTableInner"]//table[@id="T2038000001"]//')
print (el)






