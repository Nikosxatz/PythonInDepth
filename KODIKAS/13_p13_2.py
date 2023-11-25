class tmima:
    syn_foititvn=0
    syn_thesevn=0
    syn_tmimaton=0
    def __init__(self,p,t):
        self.per=p
        self.theseis=t
        self.plithos=0
        self.foitites=[]
        tmima.syn_tmimaton+=1
        tmima.syn_thesevn+=t
    def info(self):
        print('Τμήμα:',self.per,' με',self.theseis,' θέσεις και',self.plithos,'φοιτητές')
        for i in range(self.plithos):
            print(i+1,'->',self.foitites[i])
    def add(self,onoma):
        if self.plithos<self.theseis:
            self.foitites.append(onoma)
            self.plithos+=1
            tmima.syn_foititvn+=1
        else:
            print('Δεν υπάρχουν άλλες κενές θέσεις')
    def kena(self):
        k=self.theseis-self.plithos
        print('Στο',self.per,'υπάρχουν',k,'κενά')

    def taxinomisi(self):
        self.foitites.sort()

    def __del__(self):
        tmima.syn_tmimaton-=1
        tmima.syn_thesevn-=self.theseis
        tmima.syn_foititvn-=self.plithos
        
    @classmethod
    def synola(cls):
        print('Σύνολο τμημάτων:',cls.syn_tmimaton)
        print('Σύνολο φοιτητών:',cls.syn_foititvn)
        k=cls.syn_thesevn-cls.syn_foititvn
        print('Σύνολο κενών θέσεων:',k)
       
# Κυρίως πρόγραμμα
t1=tmima('ΤΠΤΕ',10)
t2=tmima('ΘΑΛΑΣΣΑΣ',20)
t1.add('Νίκος')
t1.add('Χρύσα')
t1.add('Μιχαήλ')
t1.add('Φωτεινή')
t1.taxinomisi()
t1.info()
t1.kena()
t2.add('Μαρία')
t2.add('Σπύρος')
t2.add('Πάνος')
tmima.synola()
del t2
tmima.synola()




