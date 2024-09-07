# AlphaPi

Attention: The hardware version and firmware of the AlphaPi circuit board are constantly being updated. The firmware for this project is a relatively old version, so please be sure to extract the firmware version on your own board and make a backup first!

Official Website:

http://lingxi.hetao101.com/alphapi


The firmware extracts 4M flash using the following command:

```shell
~/Library/Arduino15/packages/esp32/tools/esptool_py/4.2.1/esptool -p /dev/cu.usbmodem101 read_flash 0 0x400000 flash_contents.bin
```

Disassemble .mpy files using:
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

# APIs and Docs
## control_board_v1.mpy

### Functions

* control_board_v1.led_show_bytes(bytearray)

Use an I2C extension chip to light up a 5x5 red LED with a parameter of a 5-digit bytearray. This is a synchronization interface.
bytearray([8, 0, 0, 0, 0]) Turn on the light in row 5, column 1, bytearray([16, 0, 0, 0, 0]) Turn on the light in row 4, column 1, Similarly, bytearray([128, 0, 0, 0, 0]) Turn on the light in row 1, column 1, bytearray([255, 255, 255, 255, 255]) Turn on all lights of 5x5.

```python
import control_board_v1
# Turn on all the lights in the bottom row
control_board_v1.led_show_bytes(bytearray([8, 8, 8, 8, 8]))
```

* control_board_v1.led_show_bytes_async(bytearray)
As above, this is an asynchronous interface.
```python
import control_board_v1
control_board_v1.led_show_bytes_async(bytearray([9, 8, 0, 0, 0]))
```


### Classes
* control_board_v1.PlayRecordMission

### Examples
* 01 5X5 LED(OFFICAL METHODS)
* 02 ACEL
* 03 BUTTON
* 04 5X5 LED(WITH SOURCE CODE)


# GPIO correspondence
Known：  
button a ————— GPIO 10  
button b ————— GPIO 20  
button c ————— GPIO 21  
I2C (SC7A20 domestic three-axis) -- SDA 6 SCL 7
UART ————— TX 8 RX 9 baudrate 460800
There is also a domestically produced MCU on the board, which mainly achieves audio recording and playback, 5x5 LED functions through UART communication.
Unknown：  
P1 ————— GPIO5  
P2 ————— GPIO4    
At this point, the hardware of alphapi has been basically excavated, and it is indeed the first time to see this method of power supply through screw posts.  
TODO
