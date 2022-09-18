# AlphaPi

Disassemble .mpy files using:
```shell
$ micropython/tools/mpy-tool.py -d ./rootfs/control_board_v1.mpy  > ./rootfs/control_board_v1.mpy.txt
```

# APIs and Docs
## control_board_v1.mpy

### Functions

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


### Classes
* control_board_v1.PlayRecordMission

TODO
