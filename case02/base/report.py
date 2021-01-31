import unittest,os
from datetime import date,datetime
from HtmlTestRunner import HTMLTestRunner
from case02.base.log import logger
from case02.config.read_ini import unittest_path,report_path
from case02.base.sendemail import sendemail
class report:
    def toreport(self):
        logger().info('开始读取unittest测试核心目录')
        base_path=os.path.dirname(os.path.abspath(__file__))
        dir_path=os.path.join(base_path,unittest_path)
        print(dir_path)
        logger().info('开始discover到测试')
        try:
            discover=unittest.defaultTestLoader.discover(dir_path,pattern='*.py')
        except Exception as e:
            logger().error("加载测试用例路径失败，请查看报错原因：{0}".format(e))
        #报告命名加上时间格式
        logger().info('设置报告名称格式')
        time=datetime.now()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        #报告绝对路径
        reportname=os.path.join(base_path,report_path)+now
        reportpath=reportname+'result.html'
        #打开文件，写入测试结果
        logger().info('执行测试用例开始.......')
        try:
            #
            f=open(reportpath,'a')
            runner=HTMLTestRunner(stream=f,verbosity=2,report_title='接口用例测试报告')
            runner.run(discover)
            f.close()
            logger().info('写入报告成功')
        except Exception as e:
            logger().error("执行用例失败，请查看报错原因：{0}".format(e))

        logger().info("执行测试用例结束。。。。。。。。。。。。。")
        sendemail().send_mail(reportpath)

if __name__=='__main__':
    report().toreport()