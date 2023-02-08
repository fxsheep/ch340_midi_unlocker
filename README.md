# ch340_midi_unlocker
Turning WCH CH340 into CH345
## TL;DR: CH340G/T to CH345
First, check chip version:
```
$ ./util/read_version.py 
Version: 0x31-0x00
```
Tested on `0x31-0x00`. Continue at your own risk if it's not.  

Then patch SRAM & re-enumerate:
```
$ ./util/datamem_write.py 0x3e 0x2d 0x24 0xd0
ret:  0
$ sudo usbreset 1a86:7523
```

Check if it's working:
```
$ aplaymidi -l
 Port    Client name                      Port name
 ...
 20:0    CH345                            CH345 MIDI 1
```

Now `TXD` and `RXD` on CH340 has become `MOUT` and `MIN` on CH345.  

Note that this patch is not persistent, i.e. it has to be repeated again if CH340 is reset/power-cycled.

## TODO
 - Some fancy scripts allowing easy dumping/reading/writing CH340 data space via debug commands
 - Brute-force CH340 data space, sort out definitions of SFRs and variables in SRAM.
 - Toggle UARTs, GPIOs directly via data space access, for fun and pleasure 
 - Make a tool that patches SRAM on the fly, which changes VID/PID and make CH340 believe it's CH345, then trigger a USB re-enumeration on the host system.
 - Use return-oriented-programming to execute (partially) arbitrary code on the WCH 8bit RISC CPU in CH340, dump the code ROM and cross check with existing optical ROM extraction results.

## Documentation
See [doc](https://github.com/fxsheep/ch340_midi_unlocker/tree/main/doc)

## References
 - [Pulling Bits From ROM Silicon Die Images: Unknown Architecture](https://ryancor.medium.com/pulling-bits-from-rom-silicon-die-images-unknown-architecture-b73b6b0d4e5d)
 - [WCH CH340 datasheet](https://www.wch.cn/downloads/CH340DS1_PDF.html)
 - [WCH CH345 datasheet](https://www.wch.cn/downloads/CH345DS1_PDF.html)
 - [WCH CH534 datasheet](https://www.wch.cn/downloads/CH534DS0_PDF.html)
 - [WCH CH341 Serial driver for Linux](https://www.wch.cn/downloads/CH341SER_LINUX_ZIP.html)
