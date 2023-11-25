with open('stoixeia2.txt','r') as ff:
    Lst=[]
    while True:
        onoma=ff.read(30)
        if onoma=='':
            break
        ff.read(13)
        ypsos=float(ff.read(6))
        ff.read(4)
        Lst.append((ypsos,onoma))
Lst.sort(reverse=True)
om=open('omada.txt','w')
for t in Lst:
    if t[0]>=1.85:
        om.write(t[1]+' '+str('{:5.2f}'.format(t[0]))+'\n')
om.close()

