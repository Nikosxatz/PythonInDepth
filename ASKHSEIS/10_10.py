''' 
Τα στοιχεία της λίστας που ακολουθεί είναι οι ακολουθίες Μορς των λατινικών χαρακτήρων: A,B,C,D,E,F,G,H,I στη πρώτη σειρά
J,K,L,M,N,O,P,Q,R στη δεύτερη σειρά
S,T,U,V,W,X,Y,Z στη τρίτη σειρά 
'''

morslist=['.-','-...','-.-.','-..','.','..-.','--.','....','..',
'.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
'...','-','..-','...-','.--','-..-','-.--','--..']
mors=dict()
ascii=65
for m in morslist:
	mors.update({m:chr(ascii)})
	ascii=ascii+1
mors_frace=input('Δώσε ακολουθία mors >')
words=mors_frace.rsplit('       ')
for w in words:
	letters=w.rsplit('   ')
	for l in letters:
		ch=mors.get(l)
		if ch!= None:
			print(ch,end='')
		else:
			print('*** Το σήμα χάθηκε ***',end='')
	print(' ')


