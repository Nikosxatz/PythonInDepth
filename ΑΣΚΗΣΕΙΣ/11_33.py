fin=open('code','rb')
arx=int(input('Δώσε αρχική θέση >'))
fin.seek(arx)
while True:
    ch=fin.read(1).decode('greek')
    print(ch,end='')
    nxt=fin.read(2)
    next_pos=int.from_bytes(nxt,'little')
    if next_pos==0:
        break
    fin.seek(next_pos)
fin.close()

