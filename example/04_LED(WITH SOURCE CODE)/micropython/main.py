import machine
import time
from machine import SoftI2C, Pin

uart = machine.UART(1, 460966, tx = 8, rx = 9, timeout=200)
i2c = SoftI2C(scl=Pin(7), sda=Pin(6), freq=400000)

number_map=[
bytearray([0xf8,0x88,0x88,0x88,0xF8]),
bytearray([0,0,0xf8,0,0]),
bytearray([0xb8,0xa8,0xa8,0xa8,0xe8]),
bytearray([0xa8,0xa8,0xa8,0xa8,0xf8]),
bytearray([0xe0,0x20,0x20,0x20,0xf8]),
bytearray([0xe8,0xa8,0xa8,0xa8,0xb8]),
bytearray([0xf8,0xa8,0xa8,0xa8,0xb8]),
bytearray([0x80,0x80,0x80,0x80,0xf8]),
bytearray([0xf8,0xa8,0xa8,0xa8,0xf8]),
bytearray([0xe0,0xa0,0xa0,0xa0,0xf8]),
]
letter_map=[]

def calc_checksum(data : bytearray):
    sum = 0
    for i in range(0,len(data)-1):
        sum+=data[i]
    return sum&0xff

def uart_write(addr, data:bytearray) -> num:
    #与国产MCU通信，格式为头帧0x90+地址+数据长度+数据+累加和校验值
    #如通信成功会返回3bytes数据b'\x91\x08\x05',有时通信会卡死，原因未知，连续写两次则必定成功，奇怪？？？
    if(len(data)==0):
        return False
    byteToWrite = bytearray([0x90])
    byteToWrite.append(addr)
    byteToWrite.append(len(data))
    byteToWrite.extend(data)
    byteToWrite.append(0)
    byteToWrite[len(byteToWrite)-1]=calc_checksum(byteToWrite)
    for i in range(0,2):
        uart.write(byteToWrite)    
        ansbytes = uart.read(3)
        try:
            if len(ansbytes)==3:
                return ansbytes[2]
            else:
                print("write error: ", ansbytes)  
                return False
        except:
            pass

def led_rect():
    databytes = bytearray([0xf8,0xf8,0xf8,0x88,0xF8])
    uart_write(0x08, databytes)
    return
    
def led_array_demo():
    databytes = bytearray([0xf8,0xf8,0xf8,0xf8,0xf8])
    for i in range(0,10):
        for j in range(0,5):
            databytes[j]=databytes[j]<<1
            if databytes[j] == 0:
                databytes[j] = 0x08
        uart_write(0x08, databytes)
        time.sleep_ms(100)
    return

def show_number(n):
    uart_write(0x08, number_map[n])
    
for i in range(0,10):
    show_number(i)
    time.sleep(0.5)



