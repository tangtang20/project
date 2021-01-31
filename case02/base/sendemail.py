import smtplib
from email.header import Header
from email.mime import text
from email.mime.text import MIMEText
from case02.base.log import logger
from case02.config.read_ini import ReadIni

class sendemail:
    def send_mail(self,path):
        logger().info('测试报告邮件开始发送流程.....')
        logger().info('读取html报告页面')
        try:
            f=open(path,'rb')
            logger().info('开始读取html报告内容')
            mail_body=f.read()
            f.close()
            logger().info('读取邮件配置信息')
            #邮箱地址
            host=ReadIni('../config/config','email','host')
            #邮箱端口号
            port=ReadIni('../config/config','email','port')
            #邮箱账号
            sender=ReadIni('../config/config','email','sender')
            #邮箱授权码
            pwd=ReadIni('../config/config','email','pwd')
            #邮箱收件人
            receiver=ReadIni('../config/config','email','receiver')
            # 设置邮件正文，这里是支持HTML的
            msg=MIMEText(mail_body,'HTML','utf-8')
            # 设置邮件标题
            msg['subject']='接口自动化测试报告'
            #设置发送人
            msg['from']=sender
            #设置接收人
            msg['to']=receiver
            s=smtplib.SMTP_SSL(host,port)
            logger().info('登录邮箱')
            s.login(sender,pwd)
            logger().info('发送邮件')
            s.sendmail(sender,receiver,msg.as_string())
            logger().info('邮件发送成功')

        except Exception as e:
            logger().error('测试邮件发送失败，错误信息：{0}'.format(e))
