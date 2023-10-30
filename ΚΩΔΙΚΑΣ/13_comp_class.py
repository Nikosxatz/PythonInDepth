class etaireia:
    def __init__(self,e='NoName',p='',t=''):
        self.eponymia=e
        self.polis=p
        self.tilefono=t
        print('Η εταιρεία',self.eponymia,'δημιουργήθηκε')
    def stoixeia(self):
        print('Εταιρεία:',self.eponymia)
        print('Πόλη:',self.polis)
        print('Τηλέφωνο:',self.tilefono)
    def __del__(self):
        print('Η εταιρεία',self.eponymia,'καταστράφηκε')

class proion:
    def __init__(self,p,t):
        self.perigrafi=p
        self.timi=t
        self.promitheftis=etaireia()
        print('Το',self.perigrafi,'γεννήθηκε')
    def stoixeia(self):
        print('Είμαι ένα',self.perigrafi,'με τιμή',self.timi)
    def __del__(self):
        print('Το',self.perigrafi,'μας άφησε χρόνους')

# Κυρίως πρόγραμμα
p1=proion('πουκάμισο',45)
p2=proion('ρολόι',125)
p2.promitheftis.eponymia='ROLEX'
p2.promitheftis.stoixeia()
p1.promitheftis=etaireia('AEGEAN','Αθήνα','2102564543')
del p1


