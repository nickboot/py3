# coding:utf-8
"""
调用chrome打开网页
"""
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
url = "http://lpl.qq.com"
browser.get(url)
browser.implicitly_wait(30)     #隐式等待查找等位元素30秒
sleep(5)
print ("退出浏览器")
browser.quit()
