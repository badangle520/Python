#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import time
from email.mime.text import MIMEText
import smtplib
import urllib

mailto_list=["xx@126.com"]  #To address

mail_host="smtp.126.com"    #Set server
mail_user="xx"              #用户名
mail_pass="xx"              #密码
mail_postfix="126.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list: to address
    sub:subject
    content:content
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.starttls() # TLS need this
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
current_ip = None
def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip
'''
def getip():
    f = urllib.urlopen("http://www.canyouseeme.org/")
    html_doc = f.read()
    f.close()
    m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html_doc)
    print m.group(0)
    data=m.group()
    return data
'''
if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            #print ip
            if current_ip != ip:
                if send_mail(mailto_list,"Raspberry Pi external ip address", 'Raspberry Pi External IP Addreds is ' + ip + ' ...!'):
                    current_ip = ip
                    #print('Send OK')
        except Exception, e:
            print e
            pass
        time.sleep(60) # Check the ip address every one minute