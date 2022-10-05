import machine
import time
import os
import esp
import protocal as p

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
        while (length > 1024*64):
            fo.write(readFile(1024*64))
            length = length - 1024*64
        fo.write(readFile(length))
        fo.close()

files = os.listdir()
if(len(files) < 10):
    get_files_from_flash()       
p.check_hardware()
