fin=open('in.txt','r')
fout=open('out.txt','wb')
while True:
	onoma=readline()
	if onoma=='':
		break
	etos=int(fin.readline())
	fout.write(onoma.ljust(20))
	fout.write(etos)
fin.close()


