import idaapi
import idc
import struct


def get_filename():
    return idaapi.get_root_filename()


bin = ""

filename = "dump_%s_.bin" % (get_filename())
file = open(filename,"wb")

for ea in range(0x,0x,4):
    bin += struct.pack("<L", idc.Dword(ea))

file.write(bin)

file.close()


print "dump finish"
