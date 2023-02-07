# ch340_midi_unlocker
Turning WCH CH340 into CH345
## TODO
 - Some fancy scripts allowing easy dumping/reading/writing CH340 data space via debug commands
 - Brute-force CH340 data space, sort out definitions of SFRs and variables in SRAM.
 - Toggle UARTs, GPIOs directly via data space access, for fun and pleasure 
 - Make a tool that patches SRAM on the fly, which changes VID/PID and make CH340 believe it's CH345, then trigger a USB re-enumeration on the host system.
 - Use return-oriented-programming to execute (partially) arbitrary code on the WCH 8bit RISC CPU in CH340, dump the code ROM and cross check with existing optical ROM extraction results.
## References
 - [Pulling Bits From ROM Silicon Die Images: Unknown Architecture](https://ryancor.medium.com/pulling-bits-from-rom-silicon-die-images-unknown-architecture-b73b6b0d4e5d)
 - [WCH CH340 datasheet](https://www.wch.cn/downloads/CH340DS1_PDF.html)
 - [WCH CH345 datasheet](https://www.wch.cn/downloads/CH345DS1_PDF.html)
 - [WCH CH534 datasheet](https://www.wch.cn/downloads/CH534DS0_PDF.html)
