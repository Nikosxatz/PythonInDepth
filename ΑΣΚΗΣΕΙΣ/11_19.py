input_file=input('Δώσε όνομα αρχείου >')			# Δοκιμάστε το bath1.txt
fin=open(input_file,'r',encoding='utf-8')
fep=open('epit.txt','w',encoding='utf-8')
fap=open('apot.txt','w',encoding='utf-8')
pl=0
ep=0
for line in fin:
    pl=pl+1
    fields=line.split(',')
    if float(fields[1])>=5:
        fep.write(fields[0])
        fep.write('\n')
        ep=ep+1
    else:
        fap.write(fields[0])
        fap.write('\n')
fin.close()
fep.close()
fap.close()
print('Πλήθος φοιτητών :',pl,'Ποσοστό επιτυχίας :',ep/pl*100,'%')
