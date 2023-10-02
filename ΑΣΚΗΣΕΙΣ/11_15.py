fin=open('numbers.txt','r',encoding='cp1253')
sum=0
pl=0
while True:
    s=fin.readline()
    if s=='':
        break
    ar=float(s)
    pl=pl+1
    if pl==1:
        min=ar
        max=ar
    elif ar>max:
        max=ar
    elif ar<min:
        min=ar
    sum=sum+ar
fin.close()
print('Αθροισμα :','{:4.1f}'.format(sum))
print('Μέσος όρος :','{:4.1f}'.format(sum/pl))
print('Μέγιστος :',max)
print('Ελάχιστος :',min)

    

    
