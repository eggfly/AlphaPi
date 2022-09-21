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


def proc_1(proc_1_var_0):
    actuator_led.pixelShowU(proc_1_var_0, DataStruct(255))
    yield False


def Loop1():
    actuator_led.InitNP(5)
    actuator_led.ShowRainbow()
    while True:
        proc_1_loop = proc_1(DataStruct(control_board_v1.read_volume()))
        proc_1_loop_has_next = True
        while (proc_1_loop_has_next):
            proc_1_loop_has_next = next(proc_1_loop)
            yield True
        yield True
    yield False


loop1 = Loop1()
loop1HasNext = True


while True:
    control_board_v1.UpdateButtonStatus()
    next(soundLoop)
    if loop1HasNext:
        loop1HasNext = next(loop1)


