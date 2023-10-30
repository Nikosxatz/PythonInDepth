inp=open('bathmoi.txt','r',encoding='utf-8')
out=open('epit.txt','w',encoding='utf-8')
for line in inp:
    s=0
    lst=line.split()
    for i in range(1,4):
        s=s+float(lst[i])
        mo=s/3
    if mo>=5:
        out.write(lst[0]+' '+'{:4.2f}'.format(mo)+'\n')
out.close()
inp.close()
