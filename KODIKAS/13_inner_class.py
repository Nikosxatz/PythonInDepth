class proion:
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        self.promitheftis=proion.etaireia()
        print('Το',self.perigrafi,'γεννήθηκε')
    def stoixeia(self):
        print('Είμαι ένα',self.perigrafi,'με τιμή',self.timi)
    def __del__(self):
        print('Το',self.perigrafi,'μας άφησε χρόνους')
    class etaireia:
        def __init__(self,e='NoName',p='',t=''):
            self.eponymia=e
            self.polis=p
            self.tilefono=t
            print('H etaireia',self.eponymia,'δημιουργήθηκε')
        def stoixeia(self):
            print('Εταιρεία:',self.eponymia)
            print('Πόλη:',self.polis)
            print('Τηλέφωνο:',self.tilefono)
        def __del__(self):
            print('H etaireia',self.eponymia,'καταστράφηκε')

# Κυρίως πρόγραμμα
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
p2.promitheftis.eponymia='ROLEX'
p2.promitheftis.stoixeia()
p2.promitheftis=proion.etaireia('AEGEAN','Αθήνα','2102564543')
e1=proion.etaireia('MICROSOFT','Redmond','+011345444665')
e1.stoixeia()



