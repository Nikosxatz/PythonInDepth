fin=open('randoms.txt','r',encoding='cp1253')
fout1=open('mar.txt','w')
fout2=open('zar.txt','w')
while True:
    s=fin.readline()
    if s=='':
        break
    ar=int(s)
    if ar%2==0:
        fout2.write(str(ar))
        fout2.write('\n')
    else:
        fout1.write(str(ar))
        fout1.write('\n')
fin.close()
fout1.close()
fout2.close()
    

    
