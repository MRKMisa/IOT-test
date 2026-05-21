from gpiozero import LED
import time

led1 = LED(15)

while True:
    print(f"ON \r", end="")
    led1.on()

    time.sleep(1)
    led1.off()
    print(f"OFF\r", end="")

    time.sleep(1)