#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import urllib
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT)'
headers = {}
headers['User-Agent'] = user_agent
url = 'http://members.3322.org/dyndns/getip'   # 通过这个接口获取公网IP地址
req = urllib2.Request(url, headers = headers)
res = urllib2.urlopen(req)

ip = string.strip(res.read())   # 去除空格
print ip

fromaddr = "1915467978@qq.com"  # 填写你的发信邮箱
toaddr = "ywy86898858@126.com"   # 填写你的收信地址
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'rasperberry IP is ' + ip   # 邮件标题

body = 'rasperberry IP is ' + ip   # 邮件内容，同标题
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.qq.com', 25)   # 填写qq邮箱的发信服务器地址
server.starttls()
server.login(fromaddr, "shdzwzszxsybchda")   # 邮箱开启smtp服务时候的授权码
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text) # 开始发邮件
print u"send ok"  # 发送成功提示
server.quit()