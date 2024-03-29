# pip freeze > requirements.txt

# luma.core==1.9.0
# luma.oled==3.2.1


# Python 3 & Python Pillow 
sudo apt install python3 python3-pip python3-dev git -y

# Adafruit Python SSD1306 
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python3 setup.py install
 
# Luma.OLED Python 
sudo apt install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5 -y
sudo -H pip3 install --upgrade luma.oled
sudo -H python3 -m pip install psutil

# I2C device
sudo apt-get install -y python-smbus i2c-tools
# 手动执行一下命令开启相应功能 Interfacing Options > P5 I2C
# raspi-config 
# 查看
# sudo i2cdetect -y 1
 
# Give write permission to the I2C device 
# sudo chmod 777 /dev/i2c-*

# 开机启动 需要配置路径
# START_BAHS = /root/raspberrypi-oled-dashboard/start.sh
chmod 777 ./start.sh
# nano /etc/rc.local
# bash /root/raspberrypi-oled-dashboard/start.sh


# nano /usr/lib/systemd/system/oled-dashboard.service
