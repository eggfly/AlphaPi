import machine
import time
import os
import esp
from machine import SoftI2C, Pin

uart = machine.UART(1, 460800, tx = 8, rx = 9, timeout=100)
i2c = SoftI2C(scl=Pin(7), sda=Pin(6), freq=400000)
def calc_checksum(data : bytearray):
    sum = 0
    for i in range(0,len(data)-1):
        sum+=data[i]
    return sum&0xff
def uart_write(addr, data:bytearray) -> num:
    if(len(data)==0):
        return False
    byteToWrite = bytearray([0x90])
    byteToWrite.append(addr)
    byteToWrite.append(len(data))
    byteToWrite.extend(data)
    byteToWrite.append(0)
    byteToWrite[len(byteToWrite)-1]=calc_checksum(byteToWrite)
    uart.write(byteToWrite)    
    bytes = uart.read(3)
    if len(bytes)==3:
        return bytes[2]
    else:
        print("write error: ", bytes)  
        return False

def led_rect():
    bytes = bytearray([0xf8,0x88,0x88,0x88,0xF8])
    uart_write(0x08, bytes)
    return
    
def led_array_demo():
    bytes = bytearray([0x80,0x40,0x20,0x10,0x08])
    for i in range(0,10):
        for j in range(0,5):
            bytes[j]=bytes[j]<<1
            if bytes[j] == 0:
                bytes[j] = 0x08     
        uart_write(0x08, bytes)
        time.sleep_ms(100)
    return
    
addr = 0x160000
def readFile(length:numbers):
    global addr
    temp_buf = bytearray(length)
    esp.flash_read(addr, temp_buf)
    addr+=length
    return temp_buf
    
def get_files_from_flash():
    status = 0
    length = 0
    while(True):
        length = 0;
        if(status ==0):
            length = int.from_bytes(readFile(4), 'big')
        if(length > 1000000):
            break;
        filename = readFile(28)
        while(filename[len(filename)-1]==0xff):
            filename = filename[0:len(filename)-1]
        filename = filename.decode()
        print(filename+":"+str(length))
        fo=open(filename,'wb')
        fo.write(readFile(length))
        fo.close()

    
wav_count=0
files = os.listdir()
if(len(files) <15):
    get_files_from_flash()   
    
t=i2c.scan()
if(t[0]==18 or t[0]==24):
    led_rect()
