# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import csv#导入csv包
import sys
reload(sys)
sys.setdefaultencoding('gbk')

sys.path.append("package")
import location1

class Baidu1(unittest.TestCase):
    
    def setUp(self):
        my_file='D:\\autotest\\Python27\\test2\\data\\browser_type.csv'
        data=csv.reader(file(my_file,'rb'))
        for browser in data:
            if browser[0]!='id':        
                if browser[0]=='1' :
                    self.driver = webdriver.Firefox()
                else:
                    if browser[0]=='2' :
                        self.driver = webdriver.Chrome()
                    else:
                        if browser[0]=='3':
                            self.driver = webdriver.Ie()
                        else:
                            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
              
    #百度搜索用例
    def test_baidu_search1(self):
        u"""百度搜索1"""
        try:
            driver = self.driver
            driver.get(self.base_url )
            time.sleep(2)
            #driver.find_element_by_id("kw").send_keys("selenium webdriver1")
            location1.findId(driver,"kw").send_keys("selenium webdriver1")#调用封装的方法
            time.sleep(2)
            #driver.find_element_by_id("su").click()
            location1.findId(driver,"su1").click()
            time.sleep(3)
            #driver.close()#这里如果有这行运行会出错，因为tearDown方法里面已有类似操作
        except Exception as ex:                                          #try语句执行异常才执行
            print ex
            #取前面时间
            now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
            driver.get_screenshot_as_file("D:\\autotest\\Python27\\test2\\screen\\" + now + "error_png.png")#截图屏幕
            f=open("D:\\autotest\\Python27\\test2\\log\\log.txt",'a')  
            f.write("\n" + now + str(ex))
            f.write(u"错误截图:D:\\autotest\\Python27\\test2\\screen\\" + now + "error_png.png")  
            #f.flush()  
            f.close()
            #捕获异常后，测试报告对应用例执行结果显示erro
            raise

    #百度设置用例    
    def test_baidu_set1(self):
        u"""百度设置1"""
        try:
            driver = self.driver
            #进入搜索设置页
            driver.get(self.base_url + "/gaoji/preferences.html")
            time.sleep(2)
            #设置每页搜索结果为50 条
            #m=driver.find_element_by_name("NR")
            location1.findName(driver,"NR")
            time.sleep(2)
            #m.find_element_by_xpath("//option[@value='20']").click()
            location1.findXpath(driver,"//option[@value='20']").click()
            time.sleep(2)
            #保存设置的信息
            #driver.find_element_by_xpath("//input[@value='保存设置']").click()
            location1.findXpath(driver,"//input[@value='保存设置']").click()
            time.sleep(2)
            driver.switch_to_alert().accept()
        except Exception as ex:                                          #try语句执行异常才执行
            print ex
            #取前面时间
            now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
            driver.get_screenshot_as_file("D:\\autotest\\Python27\\test2\\screen\\" + now + "error_png.png")#截图屏幕
            f=open("D:\\autotest\\Python27\\test2\\log\\log.txt",'a')  
            f.write("\n" + now + str(ex))
            f.write(u"错误截图:D:\\autotest\\Python27\\test2\\screen\\" + now + "error_png.png")  
            #f.flush()  
            f.close()
            raise
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()    #默认执行所有以test开头的测试用例
    
