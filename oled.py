# coding=utf-8
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

from PIL import ImageFont

textFont = ImageFont.FreeTypeFont("./assets/UbuntuMono-R.ttf", 18)

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = ssd1306(serial)
#这里改ssd1306, ssd1325, ssd1331, sh1106

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((40, 4), "** --- **", fill="white")
    draw.text((16, 26), "Hello World", fill="white", font=textFont)
