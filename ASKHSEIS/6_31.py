frasi=input('Δώσε μια φράση:')
arxi=0
telos=len(frasi)-1
palindromo=True
while arxi<telos:
    while frasi[arxi]==' ':arxi+=1
    while frasi[telos]==' ':telos-=1
    if arxi>=telos:break
    print(frasi[arxi],'-',frasi[telos])
    if frasi[arxi]!=frasi[telos]:
        palindromo=False
        break
    arxi+=1
    telos-=1
if palindromo:
    print('Η φράση είναι παλύνδρομο')
else:
    print('Η φράση δεν είναι παλύνδρομο')
    
