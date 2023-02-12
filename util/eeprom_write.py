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

parser = argparse.ArgumentParser(description='Write a byte to EEPROM')
parser.add_argument('addr', type=auto_int, help='EEPROM address')
parser.add_argument('val', type=auto_int, help='Value')
parser.add_argument('--vid', type=auto_int, help='USB VID')
parser.add_argument('--pid', type=auto_int, help='USB PID')
args = parser.parse_args()

if(args.vid):
    vid = args.vid
if(args.pid):
    pid = args.pid

eepaddr = args.addr
eepval = args.val

dev = usb.core.find(idVendor=vid, idProduct=pid)
#print(dev)
if(dev):
    if(dev.is_kernel_driver_active(0)):
        dev.detach_kernel_driver(0)
    dev.set_configuration()
else:
    print("No device found. Have VID/PID been changed?")
    quit()

#Write value
print("ret: ", dev.ctrl_transfer(USB_TYPE_VENDOR | USB_RECIP_DEVICE | USB_DIR_OUT,
    CH341_REQ_EEPROM_ACC, 0x100 * eepaddr + eepval, 0xa001))

#Commit (actual write)
print("ret: ", dev.ctrl_transfer(USB_TYPE_VENDOR | USB_RECIP_DEVICE | USB_DIR_OUT,
    CH341_REQ_EEPROM_OPR, 0x000a, 0x0))

