# coding:utf8
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from luma.core.render import canvas
from PIL import ImageFont
from datetime import datetime
import time

import sysInfo


def getIP():
    return "123.123.123.123"


# 获取 CPU 温度
def getTemp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    # 读取结果，并保留两位小数
    return str(round(float(file.read()) / 1000, 2))


# def stats(oled):
#     font = ImageFont.truetype('./assets/UbuntuMono-R.ttf', 14)
#     with canvas(oled) as draw:
#         render(draw, font)


def render(draw, font):
    draw.text((0, 0), "IP: " + getIP(), font=font, fill=255)
    draw.text((0, 22), "CPU: " + getTemp() + " 'C", font=font, fill=255)
    draw.text((0, 44), datetime.now().strftime(
        "%H:%M:%S"), font=font, fill=255)


def main():
    serial = i2c(port=1, address=0x3C)
    oled = ssd1306(serial)
    font = ImageFont.truetype('./assets/UbuntuMono-R.ttf', 14)
    with canvas(oled) as draw:
        render(draw, font)


if __name__ == "__main__":

    sysInfo.getOsInfo()

    # while True:
    #     os.getOsInfo()
    #     # print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    #     # draw.text((0, 44), datetime.now().strftime(
    #     #     "%H:%M:%S"), font=font, fill=255)
    #     main()
    #     time.sleep(10)

# raw_input("Press <enter>")
