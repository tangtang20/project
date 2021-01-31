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

        except Exception as e:
            logger().error('测试邮件发送失败，错误信息：{0}'.format(e))
