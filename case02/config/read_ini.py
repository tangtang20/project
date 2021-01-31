import configparser
import os

"""
首先我们不能使用相关路径或者绝对路径的方式，这种方式只对特定的路径有效，也就是你程序写死了。
有效的解决思路是找到你文件的绝对路径，在代码中用全局变量记录下来，其他部分在此基础上进行本机或者上下级目录等操作。具体实现是：

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
注：
__file__是当前执行的文件
os.path.dirname() 是 获取路径中的目录名



这样可以使用 BASE_DIR 进行相关操作，而不用担心路径问题。
所以本次问题，有效的解决代码是：

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 读取配置文件
cfg = configparser.ConfigParser()

cfg.read(os.path.join(BASE_DIR ,'config.ini'))
注意使用os.path.join 以适应linux和windows不同目录分隔符的写法。
如果是多层级的话，可以使用os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""

#读取配置文件的内容
def ReadIni(path,section,option):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    conf=configparser.ConfigParser()
    conf.read(os.path.join(BASE_DIR,path),encoding='utf-8')
    value=conf.get(section,option)
    return value

#运行日志路径
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file=os.path.join(base_path,'log','run.log')
#日志等级
log_level=ReadIni('../config/config','log','log_level')
#unittest
unittest_path=ReadIni('config','unittest','unittest_path')
#report
report_path=ReadIni('config','report','report_path')