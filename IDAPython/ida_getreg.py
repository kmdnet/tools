from idaapi import *
from idautils import *
from idc import *


b_addr = 0x003021AA

LoadDebugger("windbg", 1)

add_bpt(b_addr,0,BPT_SOFT)
enable_bpt(b_addr,True)

StartDebugger("","","")

GetDebuggerEvent(WFNE_SUSP, -1)
addr = GetRegValue("ESI")
print "ESI : ",hex(addr)
print GetString(addr,-1,0)
 
continue_process()
