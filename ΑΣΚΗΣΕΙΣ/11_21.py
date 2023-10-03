def write_to_mo(file,polis,m):
    yparxei=False
    file.seek(0)
    for line in file:
        fields=line.split(' ')
        if fields[0]==polis:
            yparxei=True
            break
    if yparxei:
        return
    file.write(polis+' '+'{:4.1f}'.format(m)+'\n')
    

fin=open('therm1.txt','r',encoding='utf-8')
fmo=open('mo.txt','a+',encoding='utf-8')
for line in fin:
    sum=0
    fields=line.split(' ')
    for i in range(1,4):
        sum=sum+float(fields[i])
    mo=sum/3
    print(fields[0],'{:4.1f}'.format(mo))
    write_to_mo(fmo,fields[0],mo)
fin.close()
fmo.close()

