# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 取最新的测试报告
test_dir = 'F:\\work\\study\\test_dir'


def new_file():
    lists = os.listdir(test_dir)
    lists.sort(key=lambda fn: os.path.getmtime(test_dir+'\\'+fn))
    file_path = os.path.join(test_dir, lists[-1])
    return file_path


def send_email():
    f = open(new_file(), 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = 'wxyshenshou@163.com'
    password = 'wxY06130424'

    sender = 'wxyshenshou@163.com'
    receiver = '369006771@qq.com'
    subject = '测试报告'

    msg = MIMEMultipart('mixed')

    msg_html1 = MIMEText(mail_body, 'html', 'urt-8')
    msg_html1['Content-Type'] = 'application/octet-stream'
    msg_html1['Content-Disposition'] = 'attachment; filename = "results.html"'
    msg.attach(msg_html1)

    msg['From'] = 'wxyshenshou@163.com'
    msg['To'] = '369006771@qq.com'
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    try:
        send_email()
        print('send_email pass')
    except Exception as e:
        print('str(e)')
