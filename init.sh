# pip freeze > requirements.txt

# luma.core==1.9.0
# luma.oled==3.2.1

# pip install --upgrade luma.oled

# pip install -r requirements.txt

# sudo apt install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5
# sudo -H pip install --upgrade luma.oled

# Python 3 & Python Pillow 
sudo apt install python3 python3-pip python3-dev git
sudo pip3 install --upgrade setuptools wheel
sudo apt install libjpeg8-dev zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev -y
sudo pip3 install pillow --global-option="build_ext" --global-option="--enable-zlib" --global-option="--enable-jpeg" --global-option="--enable-freetype" --global-option="--enable-webp" --global-option="--enable-webpmux" --global-option="--enable-jpeg2000"
 
# Adafruit Python SSD1306 
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python3 setup.py install
 
# Luma.OLED Python 
sudo pip3 install --upgrade luma.oled
 
# Give write permission to the I2C device 
sudo chmod 777 /dev/i2c-*
