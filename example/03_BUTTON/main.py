from machine import Pin,SoftI2C,I2C
import time

class Button:
    def __init__(self, pin):
        
        self.pin = Pin(pin, Pin.IN)

    def get_presses(self, delay = 1):
        last_time, last_state, presses = time.time(), 0, 0
        while time.time() < last_time + delay:
            time.sleep_ms(50)
            if last_state == 0 and self.pin.value() == 1:
                last_state = 1
            if last_state == 1 and self.pin.value() == 0:
                last_state, presses = 0, presses + 1
        return presses

    def is_pressed(self, flag = 0):
        return self.pin.value() == flag

    def was_pressed(self, flag = 1):
        last_state = self.pin.value()
        if flag:
            if not last_state:
                return False
            else:
                while self.pin.value():
                    time.sleep_ms(10)
                return True
        else:
            if last_state:
                return False
            else:
                while not self.pin.value():
                    time.sleep_ms(10)
                return True

    def irq(self, handler, trigger):
        self.pin.irq(handler = handler, trigger = trigger)
        
button_a=Button(10)
button_b=Button(20)
button_c=Button(21)


while 1:
    time.sleep(0.01)
    if button_a.was_pressed():
        print('button a')
    if button_b.was_pressed():
        print('button b')
    if button_c.was_pressed():
        print('button c')
        
