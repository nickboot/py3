# coding:utf-8
"""
调用chrome打开网页
"""
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
url = "http://lpl.qq.com"
browser.get(url)
sleep(5)
print ("退出浏览器")
browser.quit()
