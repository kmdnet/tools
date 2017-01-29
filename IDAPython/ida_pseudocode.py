from idaapi import *
from idautils import *
from idc import *

func = ["sub_12A1E00"]

for x in func:
    addr = LocByName(x)
    pseudo_code = decompile(addr)

    with open(x+".c","w") as f:
        f.write(str(pseudo_code))
