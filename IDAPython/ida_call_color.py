from idaapi import *
from idautils import *
from idc import *


ea = BeginEA()
for func in Functions(SegStart(ea),SegEnd(ea)):
    func_name = GetFunctionName(func)

    if func_name.find("sub_") != -1:
        addr = LocByName(func_name)
        if addr != BADADDR:
            cross_ref = CodeRefsTo(addr,0)
            for ref in cross_ref:
                SetColor(ref,CIC_ITEM,0xff0000)

                    
