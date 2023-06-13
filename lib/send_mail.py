import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
import datetime
import os

from lib.absolute_path import absolutes_path
from lib.config import CONFIG
from lib.get_yaml import read_html


class SendEmail(object):
    def __init__(self, sender=None, password=None, subject=None, read_conf=None, cc=None):
        # 如果实例化的时候不传参，则从配置文件中读取参数值
        # 从配置文件中读取，邮件发件人
        self.sender = sender if sender is not None else CONFIG["emil"]["sender"]
        # 从配置文件中读取，发件人邮箱密码
        self.password = password if password is not None else CONFIG["emil"]["password"]
        # 从配置文件中读取，邮件主题
        self.subject = subject if subject is not None else CONFIG["emil"]["subject"]
        # 从配置文件中读取，邮件收件人
        self.read_conf = read_conf if read_conf is not None else CONFIG["emil"]["read_conf"]
        # 从配置文件中读取，邮件抄送人
        #self.cc = cc if cc is not None else int(CONFIG["emil"]["cc"])
        # 获取测试报告路径
        self.mail_path =read_html("/report/export/mail.html")

    def mail_163(self):
        content = """测试已完成！！
                    测试结果：成功！
                    """ + "测试报告地址：" + self.mail_path
        message = MIMEText(content, "plain", "utf-8")  # content 发送内容     "plain"文本格式   utf-8 编码格式
        message['Subject'] = str(datetime.datetime.now())[0:19] + '%s' % self.subject  # 邮件主题
        message['To'] = self.read_conf  # 收件人
        message['From'] = self.sender  # 发件人
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)  # 实例化smtp服务器
        smtp.login(self.sender, self.password)  # 发件人登录
        # smtp.sendmail(self.sender, [self.recver] + [self.cc], message.as_string())  # as_string 对 message 的消息进行了封装，收件人+抄送
        smtp.sendmail(self.sender, [self.read_conf], message.as_string())  # as_string 对 message 的消息进行了封装
        print("邮件发送成功")
        # smtp.close()
        smtp.quit()
SendEmail().mail_163()
