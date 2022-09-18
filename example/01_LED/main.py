import control_board_v1
import actuator_led
import sensor_infrared
import variable
import time
import math
import basic
from basic import DataStruct
from basic import wait_time


control_board_v1.led_show_bytes(bytearray([0x00, 0x00, 0x00, 0x00, 0x00]))
soundLoop = control_board_v1.play_record_loop()


def Loop1():
    control_board_v1.led_show_bytes_async(bytearray([128, 0, 0, 0, 0]))
    my_show_index = control_board_v1.showIndex
    time_waiting = wait_time(256)
    while next(time_waiting) and my_show_index == control_board_v1.showIndex:
        yield True
    yield False


loop1 = Loop1()
loop1HasNext = True


while True:
    control_board_v1.UpdateButtonStatus()
    next(soundLoop)
    if loop1HasNext:
        loop1HasNext = next(loop1)


