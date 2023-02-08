#!/usr/bin/env python3

import usb,hexdump,argparse

USB_RECIP_DEVICE       = 0x00
USB_TYPE_VENDOR        = 0x40
USB_DIR_IN             = 0x80
USB_DIR_OUT            = 0x00

CH341_REQ_READ_VERSION = 0x5F
CH341_REQ_WRITE_REG    = 0x9A
CH341_REQ_READ_REG     = 0x95

vid = 0x1a86
pid = 0x7523

def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser(description='Read chip/ROM version')
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

ver = dev.ctrl_transfer(USB_TYPE_VENDOR | USB_RECIP_DEVICE | USB_DIR_IN,
              CH341_REQ_READ_VERSION, 0, 0, 2)
print("Version: 0x%02x-0x%02x"%(ver[0], ver[1]))
