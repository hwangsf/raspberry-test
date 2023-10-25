from gpiozero import LED
from time import sleep

led = LED(24)
# led = LED("GPIO27")   # 給 GPIO 腳位，跟上一行意義相同！
# led = LED("J8:13")    # 定義為樹莓派的腳位

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)