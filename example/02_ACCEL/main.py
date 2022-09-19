from machine import Pin,SoftI2C,I2C
import time

sc7a20=I2C(scl=Pin(7),sda=Pin(6),freq=500000)
print(sc7a20.scan())
check=sc7a20.readfrom_mem(24,0x0f,1)  #chip_id=0x11
print(check)
sc7a20.writeto_mem(24,0x20,b'\x57')    #set to 100hz

def transdata(l,m):
    a=int.from_bytes(m,'big')
    b=int.from_bytes(l,'big')
    temp=a<<8|b
    temp=temp>>4
    temp=temp&0x0fff
    if temp&0x0800:
        temp=temp&0x07ff
        temp=~temp
        temp+=1
        temp=temp&0x07ff
        temp=-temp
    return temp
    
def read_accel():
    x1=sc7a20.readfrom_mem(24,0x28,1)
    x2=sc7a20.readfrom_mem(24,0x29,1)
    y1=sc7a20.readfrom_mem(24,0x2a,1)
    y2=sc7a20.readfrom_mem(24,0x2b,1)
    z1=sc7a20.readfrom_mem(24,0x2c,1)
    z2=sc7a20.readfrom_mem(24,0x2d,1)
    x=transdata(x1,x2)
    y=transdata(y1,y2)
    z=transdata(z1,z2)
    return x,y,z
    
while 1:
    x,y,z=read_accel()
    print('x:%d|y:%d|z:%d'%(x,y,z))
    time.sleep_ms(100)

        
