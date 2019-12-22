# coding:utf8
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from luma.core.render import canvas
from PIL import ImageFont
from datetime import datetime
import time
import os
import socket
from datetime import datetime
from threading import Timer


def getCpuTemp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    # 读取结果，并保留两位小数
    return str(round(float(file.read()) / 1000, 2))


def getSysInfo():
    return {
        'ip': socket.gethostbyname(socket.getfqdn(socket.gethostname())),
        'cpu_use': str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()),
        'cpu_temp': getCpuTemp()
    }


def render(draw, font):
    sys_info = getSysInfo()
    draw.text((0, 0), "IP: " + sys_info['sys_ip'], font=font, fill=255)
    draw.text((0, 22), "CPU: " +
              sys_info['sys_temp'] + " 'C", font=font, fill=255)
    draw.text((0, 44), "CPU_USE: " +
              sys_info['cpu_use'] + " %", font=font, fill=255)
    draw.text((0, 66), datetime.now().strftime(
        "%H:%M:%S"), font=font, fill=255)


def main():
    serial = i2c(port=1, address=0x3C)
    oled = ssd1306(serial)
    font = ImageFont.truetype('./assets/UbuntuMono-R.ttf', 14)
    with canvas(oled) as draw:
        render(draw, font)


def start(inc):
    # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    main()

    t = Timer(inc, start, (inc,))
    t.start()


if __name__ == "__main__":
    start(2)
