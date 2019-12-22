import os
import socket
from datetime import datetime
from threading import Timer

# 获取系统信息


def getSysInfo():
    return {
        'ip': socket.gethostbyname(socket.getfqdn(socket.gethostname())),
        'cpu_use': str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())
    }

# 打印时间函数


def printTime(inc):
    # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    sysInfo = getSysInfo()

    print(sysInfo['ip'])
    print(sysInfo['cpu_use'])

    t = Timer(inc, printTime, (inc,))
    t.start()


printTime(1)

print('hellow world')


# thisIsLove=input()
# if thisIsLove:
#   input ("Please Enter:")
