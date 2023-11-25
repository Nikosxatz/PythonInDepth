class kafetiera:
    def __init__(self,m,k=100,z=200,n=1000):
        self.marka=m
        self.kafes=k       
        self.zaxari=z
        self.nero=n
        self.kafedes=0

    def status(self):
        print('Μάρκα:',self.marka,end=' ')
        print('Καφές:',self.kafes,end=' ')
        print('Ζάχαρη:',self.zaxari,end=' ')
        print('Νερό:',self.nero,end=' ')
        print('Καφέδες:',self.kafedes)

    def ginetai(self,k,z,n):
        if ( self.kafes>=k and self.zaxari>=z and self.nero>=n):
            return True
        else:
            return False

    def sketos(self,ar=1):
        if self.ginetai(15*ar,0,100*ar):
            self.kafes=self.kafes-15*ar
            self.nero=self.nero-100*ar
            self.kafedes=self.kafedes+ar
            if ar>1:
                print('Ετοιμοι οι',ar,'σκέτοι .....')
            else:
                print('Ετοιμος ο σκέτος .....')
        else:
            print('Δεν υπάρχουν υλικά!')

    def metrios(self,ar=1):
        if self.ginetai(10*ar,10*ar,100*ar):
            self.kafes=self.kafes-10*ar
            self.zaxari=self.zaxari-10*ar
            self.nero=self.nero-100*ar
            self.kafedes=self.kafedes+ar
            if ar>1:
                print('Ετοιμοι οι',ar,'μέτριοι .....')
            else:
                print('Ετοιμος ο μέτριος .....')
        else:
            print('Δεν υπάρχουν υλικά!')

    def glykos(self,ar=1):
        if self.ginetai(10*ar,20*ar,100*ar):
            self.kafes=self.kafes-10*ar
            self.zaxari=self.zaxari-20*ar
            self.nero=self.nero-100*ar
            self.kafedes=self.kafedes+ar
            if ar>1:
                print('Ετοιμοι οι',ar,'γλυκοί .....')
            else:
                print('Ετοιμος ο γλυκός .....')
        else:
            print('Δεν υπάρχουν υλικά!')   
 

# Κυρίως πρόγραμμα
kaf1=kafetiera('Philips')
kaf1.status()
kaf1.sketos(3)
kaf1.sketos()
kaf1.status()
kaf1.metrios(2)
kaf1.glykos()
kaf1.status()
kaf1.metrios(15)
kaf2=kafetiera('Kenwood',200,400,2000)
kaf2.status()
