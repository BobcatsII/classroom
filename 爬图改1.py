#!/usr/bin/python
#-*- coding:utf-8 -*-

#导入正则模块
#导入线程模块
#导入请求模块
#导入系统模块

import re
import thread
import requests
import os

#获取html页面参数
def getHtml(url):
    r = requests.get(url)
#注意r.text的用法
    html = r.text
    return html

#判断当前目录是有含有 ‘path’ 的目录
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

#保存图片
def saveImages(html, name):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    for imageURL in imglist:
        splitPath = imageURL.split('/')
        fileName = splitPath[-1]
        print fileName, 'Download Complete'
        dirName = name + "/" + fileName
        try:
            if "http:" in imageURL:
                rr = requests.get(imageURL)
            else:
                rr = requests.get('http:' + imageURL)
            data = rr.content
            with open(dirName, 'wb+') as f:
                f.write(data)
        except:
            continue

if __name__ == '__main__':
    num1 = input('The initial page: ')
    num2 = input('The final page: ')
    print 'Start Downloading...'
    path = 'Picture'
    mkdir(path)
    for i in range(num1,num2+1):
        html = getHtml("http://jandan.net/ooxx/page-%d#comments" % i)
        thread.start_new_thread(saveImages, (html, path))
    raw_input('press Enter to exit...\n')

