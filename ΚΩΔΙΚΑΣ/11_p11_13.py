import sys

fout=open('edit.txt','w',encoding='utf-8')
pl=0
for i in sys.stdin:
    fout.write(i)
    sys.stdout.write('Εγγράφηκε γραμμή με '+str(len(i))+' χαρακτήρες\n')
    pl+=1

sys.stdout.write('Στο αρχείο εγγράφηκαν '+str(pl)+' γραμμές')
fout.close()
