# -*- coding: utf-8 -*-
from selenium import webdriver
'''
本文件简易的封装定位单个元素和定位一组元素的方法
'''
class Location2:
    '''定位单个元素封装'''
    def findId(self,driver,id):
        f = driver.find_element_by_id(id)
        return f
    def findName(self,driver,name):
        f = driver.find_element_by_name(name)
        return f
    def findClassName(self,driver,name):
        f = driver.find_element_by_class_name(name)
        return f
    def findTagName(self,driver,name):
        f = driver.find_element_by_tag_name(name)
        return f
    def findLinkText(self,driver,text):
        f = driver.find_element_by_link_text(text)
        return f
    def findPLinkText(self,driver,text):
        f = driver.find_element_by_partial_link_text(text)
        return f
    def findXpath(self,driver,xpath):
        f = driver.find_element_by_xpath(xpath)
        return f
    def findCss(self,driver,css):
        f = driver.find_element_by_css_selector(css)
        return f
    '''定位一组元素封装'''
    def findsId(self,driver,id):
        f = driver.find_elements_by_id(id)
        return f
    def findsName(self,driver,name):
        f = driver.find_elements_by_name(name)
        return f
    def findsClassName(self,driver,name):
        f = driver.find_elements_by_class_name(name)
        return f
    def findsTagName(self,driver,name):
        f = driver.find_elements_by_tag_name(name)
        return f
    def findsLinkText(self,driver,text):
        f = driver.find_elements_by_link_text(text)
        return f
    def findsPLinkText(self,driver,text):
        f = driver.find_elements_by_partial_link_text(text)
        return f
    def findsXpath(self,driver,xpath):
        f = driver.find_elements_by_xpath(xpath)
        return f
    def findsCss(self,driver,css):
        f = driver.find_elements_by_css_selector(css)
        return f 
