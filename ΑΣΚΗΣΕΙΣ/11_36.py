fin=open('foit.txt','r')
fout=open('out1.txt','w')
Lst=[]
while True:
	onoma=fin.readline()
	if onoma=='':
		break
	Lst.append(onoma)
Lst.sort()
fin.close()
fout.writelines(Lst)
fout.close()

