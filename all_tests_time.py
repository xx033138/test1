# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import os ,time,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import sys
reload(sys)
sys.setdefaultencoding('gbk')#不添加如上三行的话，print中文会显示乱码

sys.path.append("test_case\\package")#将封装方法路径加入系统路径
#import location



#定义发送邮件
def sentmail(file_new):
    #发信邮箱
    #mail_from=u"秦超<18800239@qq.com>"
    mail_from="18800239@qq.com"
    #收信邮箱
    mail_to="496626212@qq.com,460542845@qq.com,18800239@qq.com"
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEMultipart()
    #定义标题
    msg['Subject']=u"百度测试报告"
    msg['From']=mail_from
    msg['To']=mail_to
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

    

    #邮件正文
    textpart=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(textpart)
    #邮件附件
    htmlpart = MIMEApplication(open(file_new, 'rb').read())
    htmlpart.add_header('Content-Disposition', 'attachment', filename=file_new.split('\\')[5])
    msg.attach(htmlpart)
    try:
        smtp=smtplib.SMTP_SSL('smtp.qq.com',465)
        #连接 SMTP 服务器，此处用的qq的 SMTP 服务器
        #smtp.connect('smtp.qq.com',465)
        #用户名密码
        smtp.login('18800239@qq.com','krwivjhrcncrbhfb')#授权码，非邮箱密码
        smtp.sendmail(mail_from,mail_to.split(','),msg.as_string())
        smtp.quit()
        print (u'邮件已经发送 !')
    except smtplib.SMTPException,e:
        print (u'失败:%s'%e)

#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'D:\\autotest\\Python27\\test2\\report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    sentmail(file_new)


startlist='D:\\autotest\\Python27\\test2\\test_case'
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义.如果没顶层目录（也就是说测试用例不是放在多级目录中），默认为 None。
    discover=unittest.defaultTestLoader.discover(startlist,pattern ='start_*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit 
    return testunit




alltestnames = creatsuitel()
#定义个报告存放路径，支持相对路径
#取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#把当前时间加到报告中
filename = "D:\\autotest\\Python27\\test2\\report\\" + now +"result.html"
fp = file(filename, 'wb')
#定义测试报告
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')
if __name__ == "__main__":
    #控制脚本自动执行时间
    k=1
    while k<2:
        start_time=time.strftime('%H_%M',time.localtime(time.time()))
        #if start_time=='12_20':
        if 1==1:
            print u'开始运行脚本：'
            #执行测试用例
            runner.run(alltestnames)
            fp.close()
            #执行发邮件
            sendreport()
            print u"运行完成退出!"
            break
        else:
            time.sleep(5)
            print start_time