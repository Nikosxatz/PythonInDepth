xar=input('Δώσε κείμενο αναζήτησης -> ')
fout=open('out.txt','w',encoding='utf-8')
pl=0
with open('foit.txt','r',encoding='utf-8') as f:
    for line in f:
        if xar in line:
            fout.write(line)
            pl+=1
fout.close()
print('Στο αρχείο out.txt εγγράφηκαν ',pl,' γραμμές')
