const Display = require('oled-display');

const config = {
  driver: 'SSD1306_128_64', // Drivers: SSD1306_128_64, SSD1306_128_32, ...
  interface: 'I2C', // Interfaces: I2C, SPI
  // I2C
  i2c_bus: 0, // Often 0/1. Armbian enable in 'armbian-config'
  i2c_address: 0x3C, // If this fails, try 0x3D
  // SPI
  spi_rst_pin: 24, // Change this (SSD1306 only)
  spi_dc_pin: 23, // Change this (SSD1306 only)
  spi_port: 0, // Might need to change this
  spi_device: 0, // Might need to change this
  spi_hz: 8000000, // (SSD1306 only)
};

let frame_rate = 0; // 0 is uncapped, frames per second
async function start() {
  let display = new Display(config, __dirname);

  while (true) {
    try {
      display.clear(); // Color: clear(0/1)

      // Draw here
      display.drawRectangleSize(0, 1, 0, 0, display.getWidth() - 1, display.getHeight() - 1); // Display border
      display.drawText(1, 'HELLO WORLD!', 3, 2, 1, 1); // Horizontally aligned right

      await display.render(10000); // Timeout after timeout of 10 seconds
      await display.sync(frame_rate); // Sync's to backend as well as framerate
    }
    catch (e) {
      if (e instanceof Display.Error) {
        console.error(e.name + ',', e.status + ',', e.message);
        process.exit(1);
      } else
        throw e;
    }
  };
};

start();