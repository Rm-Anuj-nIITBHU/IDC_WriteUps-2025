key = "xor_is_love"
flag_enc = "{mob@XmCv]zZ[MFPYpJEokZ@_FTDuJvRzmHsoF_`yE_qUvJuBJFRFo}@\X|EBkELom[NDm^"
output = ""
count=0;
while count<len(flag_enc):
    output=output+(chr((ord(key[count%len(key)])-70)^ord(flag_enc[count])))
    count=count+1
print(output)