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

parser = argparse.ArgumentParser(description='Write to one or two data memory addresses')
parser.add_argument('addr', type=auto_int, help='datamem address 1 to write to')
parser.add_argument('val', type=auto_int, help='value 1 to write')
parser.add_argument('addr2', type=auto_int, nargs='?', help='datamem address 2 to write to [optional]')
parser.add_argument('val2', type=auto_int, nargs='?', help='value 2 to write [optional]')
parser.add_argument('--vid', type=auto_int, help='USB VID')
parser.add_argument('--pid', type=auto_int, help='USB PID')
args = parser.parse_args()

if(args.vid):
    vid = args.vid
if(args.pid):
    pid = args.pid

regaddr1 = args.addr
regval1 = args.val

if(args.addr2 and args.val2):
    regaddr2 = args.addr2
    regval2 = args.val2
else:
    regaddr2 = args.addr
    regval2 = args.val

dev = usb.core.find(idVendor=vid, idProduct=pid)
#print(dev)
if(dev):
    if(dev.is_kernel_driver_active(0)):
        dev.detach_kernel_driver(0)
    dev.set_configuration()
else:
    print("No device found. Have VID/PID been changed?")
    quit()

print("ret: ", dev.ctrl_transfer(USB_TYPE_VENDOR | USB_RECIP_DEVICE | USB_DIR_OUT,
    CH341_REQ_WRITE_REG, 0x100 * regaddr2 + regaddr1, 0x100 * regval2 + regval1))

