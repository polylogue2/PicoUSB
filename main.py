from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# Set up I2C for the OLED display
sda = Pin(26)
scl = Pin(27)
i2c = I2C(1, scl=scl, sda=sda, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Boot-up sequence
oled.fill(0)

# Display "PicoUSB" centered on the middle lines (vertically and horizontally)
text = "PicoUSB"
text_width = len(text) * 6  # Width of the text
text_x = (128 - text_width) // 2  # Center horizontally
text_y = (64 - 16) // 2  # Center vertically (16 pixels for the text height)
oled.text(text, text_x, text_y)

# Spinner animation below "PicoUSB"
spinner = ["\\", "/", "-", "\\"]
spinner_pos = 0

for _ in range(20):  # Repeat the spinner 20 times
    oled.fill_rect(0, 20, 128, 64, 0)  # Clear the area where spinner will go
    oled.text(text, text_x, text_y)  # Re-display "PicoUSB"
    
    # Spinner centered horizontally, placed below "PicoUSB"
    spinner_x = (128 - 6) // 2  # Center spinner horizontally
    oled.text(f" {spinner[spinner_pos]}", spinner_x, text_y + 20)  # Spinner below "PicoUSB"
    
    oled.show()
    time.sleep(0.1)  # Delay for spinner speed

    # Move to the next spinner symbol
    spinner_pos = (spinner_pos + 1) % len(spinner)

# After boot-up, the screen can be updated with the next message
oled.fill(0)
oled.text("PicoUSB v0.1", 0, 0)
oled.text("=-=-=-=-=-=-=-=-=", 0, 10)
oled.text("", 0, 20)  # Blank line
oled.text("Waiting for USB", 0, 30)
oled.text("connection...", 0, 40)
oled.show()

# Simulate waiting for USB connection (you can replace this with actual logic)
time.sleep(2)  # Wait for 2 seconds before updating the screen

# Clear the previous lines
oled.fill_rect(0, 20, 128, 44, 0)  # Clear from (0, 20) to the bottom

# Update the screen with new text
oled.text("Mass Storage [!]", 0, 20)
oled.text("HID [!]", 0, 30)
oled.show()

