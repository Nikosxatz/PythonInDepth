arxeio=input('Δώσε όνομα αρχείου > ')
ff=open(arxeio,'r',encoding='utf-8')
pedia=int(input('Πλήθος πεδίων > '))
nl=input('Αλλαγή γραμμής μεταξύ των εγγραφών Ν/Ο > ')
if nl=='N' or nl=='ν' or nl=='Ν' or nl=='n':
    nl=True
else:
    nl=False
print('Δώσε τύπο πεδίων s/i/f')
typos=[]
mikos=[]
for i in range(pedia):
    t=input('Τύπος πεδίου '+str(i+1)+':')
    typos.append(t)
    m=int(input('Μήκος πεδίου '+str(i+1)+':'))
    mikos.append(m)
synolo=0
for i in mikos:
    synolo=synolo+i
if nl:
    synolo=synolo+2
while True:
    eggrafi=int(input('Δώσε αριθμό εγγραφής >'))
    if eggrafi==0:
        break
    thesi=(eggrafi-1)*synolo
    ff.seek(thesi)
    line=[]
    for i in range(pedia):
        p=ff.read(mikos[i])
        if p=='':
            print('Δεν υπάρχει αυτή η εγγραφή')
            break
        if typos[i]=='i':
            p=int(p)
        elif typos[i]=='f':
            p=float(p)
        line.append(p)
    if line:
        print(line)
ff.close()        
        
        
