class proion:
    def __init__(self,p,t,k):
        self.perigrafi=p
        self.timi=t
        self.komatia=k
        print('Ένα',self.perigrafi,'δημιουργήθηκε')
     
    def stoixeia(self):
        print('Είμαι ένα',self.perigrafi,'με τιμή',self.timi)

    def __del__(self):
        print('To',self.perigrafi,'...μας άφησε χρόνους')
    
# Κυρίως πρόγραμμα
apothiki=[]
for i in range(5):
    print('Προϊόν',i+1)
    print('--------------------')
    pr=input('Περιγραφή :')
    tm=float(input('Τιμή :'))
    km=int(input('Τεμάχια :'))
    apothiki.append(proion(pr,tm,km))
print('====================')
axia=0
for p in apothiki:
    p.stoixeia()
    axia=axia+p.timi*p.komatia
print('Συνολική αξία αποθήκης :',axia)
del apothiki
