#!/usr/bin/env python3
# -*-coding:utf-8-*-

def sendmail():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    msg = MIMEText("邮件内容","plain", "utf-8")
    msg["From"] = formataddr(["发件人", "zyrarter@163.com"])
    msg["To"] = formataddr(["收件人", "976207292@qq.com"])
    msg["Subject"] = "邮件的主题"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("zyrarter@163.com", "zyr519328")
    server.sendmail("zyrarter@163.com", ["976207292@qq.com",], msg.as_string())
    server.quit()


sendmail()