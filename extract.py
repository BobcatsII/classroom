#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
with open('form.txt', 'r') as f:
    test = f.read()
    m = re.findall(r"[A-Za-z]+", test)
    m.sort()
    word = '\n'.join(m)
    with open('to.txt', 'w') as g:
        g.write(word)
