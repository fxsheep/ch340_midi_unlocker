#!/usr/bin/env python3

import usb,hexdump,argparse

USB_RECIP_DEVICE       = 0x00
USB_TYPE_VENDOR        = 0x40
USB_DIR_IN             = 0x80
USB_DIR_OUT            = 0x00

#EEPROM access ?
CH341_REQ_EEPROM_ACC   = 0x54
#EEPROM operation ?
CH341_REQ_EEPROM_OPR   = 0x5e

vid = 0x1a86
pid = 0x7523

def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser(description='Hexdump EEPROM')
parser.add_argument('--vid', type=auto_int, help='USB VID')
parser.add_argument('--pid', type=auto_int, help='USB PID')
args = parser.parse_args()

if(args.vid):
    vid = args.vid
if(args.pid):
    pid = args.pid

dev = usb.core.find(idVendor=vid, idProduct=pid)
#print(dev)
if(dev):
    if(dev.is_kernel_driver_active(0)):
        dev.detach_kernel_driver(0)
    dev.set_configuration()
else:
    print("No device found. Have VID/PID been changed?")
    quit()

eeprom = []

for i in range(0, 64, 8):
    eeprom = eeprom + list(dev.ctrl_transfer(USB_TYPE_VENDOR | USB_RECIP_DEVICE | USB_DIR_IN,
              CH341_REQ_EEPROM_ACC, 0x100 * i, 0xa001, 8))

hexdump.hexdump(bytes(eeprom))
