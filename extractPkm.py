def bytes_to_int(bytes, byteorder='big'):
    return int.from_bytes(bytes, byteorder)



def savPkm(f,number):
   pkm = f.read(100)
   pkmFile = open(str(number)+".pkm", "wb")
   pkmFile.write(pkm)
   pkmFile.close()



f = open("may.sav", 'rb')

offset = 0
count = 0
personalitySet = set()
ID_List=[ b'\x3f\x2e\x21\x36', b'\xcf\x5a\x2b\x0e', b'\xa1\xea\x5c\x18', b'\x89\x99\xf0\x5e', b'\x7d\x0e\x5d\xd7', b'\x52\xe1\x74\xe3', b'\x7f\x5a\xf9\x0e' ]

while True:
    buf = f.read(4)
    if not buf:
        break

    dword = bytes_to_int(buf, byteorder='little')
    for ID in ID_List:
        target_id = bytes_to_int(ID, byteorder='big')
        if dword == target_id:
            #save last position
            last_pos = f.tell()
            #reset reader to beggining of potential pkm chunk
            f.seek(last_pos-8)
            #read the unique pokemon ID num
            personalityNum = f.read(4)
            #if personalityNum has not been processed, then extract pkm, and increment count
            if personalityNum not in personalitySet:
                #reset the read head to the start of the potential pkm chunk
                f.seek(last_pos-8)
                personalitySet.add(personalityNum)
                savPkm(f, count)
                count += 1
            #reset head to the saved position
            f.seek(last_pos)

f.close()

print(count)
