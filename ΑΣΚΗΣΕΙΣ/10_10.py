morslist=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
mors=dict()
ascii=65
for m in morslist:
    mors.update({m:chr(ascii)})
    ascii=ascii+1
mors_frace=input('Δώσε ακολουθία mors >')
words=mors_frace.rsplit('       ')
for w in words:
    letters=w.rsplit('   ')
    for l in letters:
        ch=mors.get(l)
        print(ch,end='')
    print(' ')

