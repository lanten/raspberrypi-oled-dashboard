# coding:utf8
import struct
import fcntl
import time
import os
import socket
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
from datetime import datetime
from datetime import datetime
from threading import Timer

serial = i2c(port=1, address=0x3C)
oled = ssd1306(serial)
font = ImageFont.truetype('/root/raspberrypi-oled-dashboard/assets/UbuntuMono-R.ttf', 14)
draw = 0


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15]))[20:24])


def getCpuTemp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    # 读取结果，并保留两位小数
    return str(round(float(file.read()) / 1000, 2))


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])


def getSysInfo():
    ram_info = getRAMinfo()
    return {
        # 'ip_eth0': get_ip_address('eth0'),
        # 'ip_wlan0': get_ip_address('wlan0'),
        'ip': get_ip_address('eth0'),
        'cpu_use': str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()),
        'cpu_temp': getCpuTemp(),
        'ram_total': str(round(int(ram_info[0]) / 1000, 1)),
        'ram_use': str(round(int(ram_info[1]) / 1000, 1)),
        'ram_free': str(round(int(ram_info[2]) / 1000, 1))
    }


def render():
    with canvas(oled) as draw:
        offset = 16
        sys_info = getSysInfo()
        # print(sys_info)
        draw.text((0, 0), "IP: " + sys_info['ip'], font=font, fill=255)
        draw.text((0, offset*1), "CPU: " +
                  sys_info['cpu_temp'] + " 'C", font=font, fill=255)
        draw.text((0, offset*2), "USE: " +
                  sys_info['cpu_use'] + " %", font=font, fill=255)
        draw.text((0, offset*3), "RAM: " +
                  sys_info['ram_use'] + " / " + sys_info['ram_total'], font=font, fill=255)


# def main():
#     serial = i2c(port=1, address=0x3C)
#     oled = ssd1306(serial)
#     font = ImageFont.truetype('./assets/UbuntuMono-R.ttf', 14)
#     with canvas(oled) as draw:
#         render(draw, font)


def start(inc):
        # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # main()
    # sysInfo = getSysInfo()
    # print(sysInfo)
    render()

    t = Timer(inc, start, (inc,))
    t.start()


if __name__ == "__main__":
    start(1)
