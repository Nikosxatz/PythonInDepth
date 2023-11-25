import random

class karta:
    def __init__(self,f,e,t):
        self.figoura=f
        self.eidos=e
        self.timi=t

    def display(self):
        print(self.figoura,self.eidos)

    def pontoi(self):
        return self.timi

    def __gt__(self, o):
        if self.timi>o.timi:
            return True
        else:
            return False
        
class trapoula:
    def __init__(self,x,ar):
        self.xroma=x
        self.kartes=[]
        fig=('Άσσος','Δύο','Τρία','Τέσσερα','Πέντε','Έξι','Επτά','Οκτώ','Εννέα','Δέκα','Βαλές','Ντάμα','Ρήγας')
        eidi=('Καρό','Κούπα','Μπαστούνι','Σπαθί')
        for i in range(13):
            for j in range(4):
                if i<9:
                    axia=i+1
                else:
                    axia=10
                k=karta(fig[i],eidi[j],axia)
                self.kartes.append(k)
        self.kartes=self.kartes*2
        print('Μόλις δημιούργησα μια {} τράπουλα με {} κάρτες'.format(x,len(self.kartes)))
                
    def display(self):
        print('Τράπουλα :',self.xroma,'  Κάρτες :',len(self.kartes))
        print('===================================================')
        for i in self.kartes:
            i.display()
            
    def suffle(self):
        for i in range(5*len(self.kartes)):
            a=random.randint(0,len(self.kartes)-1)
            b=random.randint(0,len(self.kartes)-1)
            self.kartes[a],self.kartes[b]=self.kartes[b],self.kartes[a]
        print('Μόλις ανακάτεψα την {} τράπουλα με {} κάρτες'.format(self.xroma,len(self)))

    def get_one(self):
        krt=self.kartes.pop(0)
        return krt

    def __add__(self, o):
        nt=trapoula(self.xroma+' & '+o.xroma)
        nt.kartes=self.kartes+o.kartes
        return nt

    def __gt__(self, o):
        if len(self.kartes)>len(o.kartes):
            return True
        else:
            return False
        
    def __len__(self):
        return len(self.kartes)

class mana:
    def __init__(self,x,ar):
        self.kartes=[]
        self.kryfi_karta=None
        self.poso=0
        self.stoiva=trapoula(x,ar)
        self.stoiva.suffle()

    def display_all(self):
        print('\nΚάρτες Μάνας')
        print('================')
        s=0
        for k in self.kartes:
            k.display()
            s=s+k.pontoi()
        print('=================')
        print('Σύνολο πόντων:',s)

    def display_all_but_one(self,kryfi):
        print('\nΦανερές Κάρτες Μάνας')
        print('====================')
        s=0
        for i in range(len(self.kartes)):
            if i!=kryfi:
                self.kartes[i].display()
                s=s+self.kartes[i].pontoi()
            else:
                print('??????????????')
        print('====================')
        print('Σύνολο φανερών πόντων:',s)

    def vres_kryfi(self):
        maxpos=self.kartes.index(max(self.kartes))
        minpos=self.kartes.index(min(self.kartes))
        return minpos
        
    def trava_karta(self):
        krt=self.stoiva.get_one()
        self.kartes.append(krt)

    def dose_karta(self):
        krt=self.stoiva.get_one()
        return krt

    def pontoi(self):
        s=0
        for i in self.kartes:
            s=s+i.pontoi()
        return s

    def kerdisa(self,p):
        self.poso=self.poso+p

    def exasa(self,p):
        self.poso=self.poso-p

    def clear_hand(self):
        self.kartes.clear()
    
    def pexe_31(self,p):
        gyroi=1
        while True:
            print('\n########## ΓΥΡΟΣ No {} - Κάρτες στη στοίβα {} ##########\n'.format(gyroi,len(self.stoiva)))
            print('Μάνα: Τώρα δίνω στον παικτη {} την πρώτη κάρτα'.format(p.onoma))
            k=self.dose_karta()
            k.display()
            p.moy_edosan_karta(k)
            print('Σύνολο πόντων:',p.pontoi())
            while True:
                bet_str=input('{} δώσε το ποντάρισμά σου (1~10 euro) -> '.format(p.onoma))    
                if bet_str.isnumeric():
                    bet=int(bet_str)
                    if bet>=1 and bet<=10:       
                        break    
            print('\nΤώρα τραβάει η μάνα')
            while self.pontoi()<=23:
                self.trava_karta()
                if self.pontoi()==14: break
            if self.pontoi()==31:                
                print('Τριανταμία ... σε κέρδισα')
                self.display_all()
                self.kerdisa(bet)
                p.exasa(bet)
               
            elif self.pontoi()>31:
                print('Οπς ... κάηκα με',self.pontoi(),'πόντους')
                self.exasa(bet)
                p.kerdisa(bet)
            else:
                print('Μάνα: Τράβηξα {} κάρτες'.format(len(self.kartes)))
                self.display_all_but_one(self.vres_kryfi())
                print('\nΤώρα δίνω κάρτες στον παικτη {}'.format(p.onoma))
                while True:
                    k=p.zito_karta(self)
                    k.display()
            
                    print('Σύνολο πόντων:',p.pontoi())
                    
                    if p.pontoi()>=31: break
                    ans=input('{} πάτησε ENTER για επόμενη κάρτα - οτιδήποτε άλλο για σταμάτημα  >'.format(p.onoma))
                    if ans!='': break
                if p.pontoi()==31:
                    print('\nΜΠΡΑΒΟ ΤΡΙΑΝΤΑΜΙΑ κέρδισες!!!')
                    self.exasa(bet)
                    p.kerdisa(bet)
                elif p.pontoi()>31:
                    print('\nΔυστυχώς  κάηκες με',p.pontoi())
                    self.display_all()
                    self.kerdisa(bet)
                    p.exasa(bet)
                elif self.pontoi()==14:
                    print('\nΔυστυχώς σε κέρδισα γιατί έχω 14')
                    self.display_all()
                    self.kerdisa(bet)
                    p.exasa(bet)
                elif p.pontoi()==14:
                    print('\nΜπράβο με κέρδισες έχεις 14')
                    self.exasa(bet)
                    p.kerdisa(bet)
                elif p.pontoi()>self.pontoi():
                    print('\nΜπράβο με κέρδισες έχεις {} και έχω {} πόντους'.format(p.pontoi(),self.pontoi()))
                    self.exasa(bet)
                    p.kerdisa(bet)
                elif p.pontoi()==self.pontoi():
                    print('\nΈχουμε και οι δύο {} πόντους ... αλλά επειδή είμαι η μάνα σε κερδίζω :-)'.format(self.pontoi()))
                    self.display_all()
                    self.kerdisa(bet)
                    p.exasa(bet)
                else:
                    print('\nΔυστυχώς σε κέρδισα έχεις {} και έχω {} πόντους'.format(p.pontoi(),self.pontoi()))
                    self.display_all()
                    self.kerdisa(bet)
                    p.exasa(bet)
            if (p.poso>0):
                print('\n****** {} μέχρι τώρα κερδίζεις {} euro '.format(p.onoma,p.poso))
            elif (p.poso<0):
                print('\n****** {} μέχρι τώρα χάνεις {} euro '.format(p.onoma,-p.poso))
            else:
                print('\n****** {} μέχρι τώρα δεν κερδίζεις ούτε χάνεις ******')
            gyroi=gyroi+1
            if len(self.stoiva)<=10:
                print('Μάνα: Δεν μπορεί να γίνει άλλος γύρος παρέμειναν μόνο {} κάρτες στη στοίβα'.format(len(self.stoiva)))
                ans=input('Θέλετε να προστεθεί και άλλη τράπουλα στη στοίβα N/O >')
                if ans in 'NnΝν':
                    self.stoiva=self.stoiva+trapoula('NEA',1)
                    self.stoiva.suffle()
                else: break
            ans=input('{} πάτησε ENTER για επόμενο γύρο - οτιδήποτε άλλο για σταμάτημα  >'.format(p.onoma))
            if ans!='': break
            self.clear_hand()
            p.clear_hand()
        return p.poso

class paiktis:
    def __init__(self,o):
        self.kartes=[]
        self.onoma=o
        self.poso=0

    def display(self):
        print('\nΚάρτες παίκτη:',self.onoma)
        print('=====================')
        for k in self.kartes:
            k.display()

    def zito_karta(self,m):
        krt=m.dose_karta()
        self.kartes.append(krt)
        return krt

    def moy_edosan_karta(self,krt):
        self.kartes.append(krt)

    def pontoi(self):
        s=0
        for i in self.kartes:
            s=s+i.pontoi()
        return s

    def kerdisa(self,p):
        self.poso=self.poso+p

    def exasa(self,p):
        self.poso=self.poso-p

    def clear_hand(self):
        self.kartes.clear()    
  
# Κυρίως πρόγραμμα 
m1=mana('Κόκκινη',2)
p1=paiktis('Νίκος')
synolo=m1.pexe_31(p1)
# Εμφάνιση αποτελεσμάτων
if (synolo>0):
    print('\n****** {} κέρδισες συνολικά {} euro '.format(p1.onoma,synolo))
elif (synolo<0):
    print('\n****** {} έχασες συνολικά {} euro '.format(p1.onoma,-synolo))
else:
    print('\n****** {} ούτε κέρδισες ότε έχασες!!! ******')
