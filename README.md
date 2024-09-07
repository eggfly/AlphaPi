# AlphaPi

注意！！AlphaPi 电路板的硬件版本和固件随时都在更新，这个项目的固件是比较老的版本，请一定要先提取自己板子上的固件版本，先做好备份！

官网:

http://lingxi.hetao101.com/alphapi


固件使用如下命令提取 4M flash：

```shell
~/Library/Arduino15/packages/esp32/tools/esptool_py/4.2.1/esptool -p /dev/cu.usbmodem101 read_flash 0 0x400000 flash_contents.bin
```

使用以下命令解析 .mpy 文件：
```shell
$ micropython/tools/mpy-tool.py -d ./rootfs/control_board_v1.mpy  > ./rootfs/control_board_v1.mpy.txt
```


```shell
>>> import esp32
>>> esp32.Partition.find()
[<Partition type=0, subtype=0, address=65536, size=2031616, label=factory, encrypted=0>]
```


```shell
# flash_read:
esp.flash_read(byte_offset, length_or_buffer)¶
```

# 所有 API 和文档
## control_board_v1.mpy

### 方法

* control_board_v1.led_show_bytes(bytearray)

用 I2C 扩展芯片点亮 5x5 红色LED，参数是5个数字的bytearray。这个是同步接口。
bytearray([8, 0, 0, 0, 0]) 点亮第5行第1列的灯，bytearray([16, 0, 0, 0, 0]) 点亮第4行第1列的灯，同理，bytearray([128, 0, 0, 0, 0]) 点亮第1行第1列的灯，bytearray([255, 255, 255, 255, 255]) 点亮5x5所有的灯。

```python
import control_board_v1
# 点亮最下面一行所有的灯
control_board_v1.led_show_bytes(bytearray([8, 8, 8, 8, 8]))
```

* control_board_v1.led_show_bytes_async(bytearray)
同上，这个是异步接口。
```python
import control_board_v1
control_board_v1.led_show_bytes_async(bytearray([9, 8, 0, 0, 0]))
```


### 类
* control_board_v1.PlayRecordMission

### 示例
* 01 5X5 LED(OFFICAL METHODS)
* 02 ACEL
* 03 BUTTON
* 04 5X5 LED(WITH SOURCE CODE)


# GPIO对应
已知：  
button a ————— GPIO 10  
button b ————— GPIO 20  
button c ————— GPIO 21  
I2C(SC7A20国产三轴) ————— SDA 6 SCL 7  
UART ————— TX 8 RX 9 baudrate 460800
板子上还有个国产MCU，主要通过UART通信实现音频录制播放、5x5 led的功能。
未知：  
P1 ————— GPIO5  
P2 ————— GPIO4    
到此alphapi的硬件基本挖掘完毕，通过螺丝柱供电这种方式确实第一次见。  
TODO
