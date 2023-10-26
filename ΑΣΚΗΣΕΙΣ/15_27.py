from abc import ABC, abstractmethod
 
class oxima(ABC):
    def __init__(self,e,x,v):
        self.eidos=e
        self.xroma=x
        self.varos=v
        
    @abstractmethod
    def xekina(self):
        pass

    @abstractmethod
    def stamata(self):
        pass

    @abstractmethod
    def stripse_aristera(self):
        pass
    
    @abstractmethod
    def stripse_dexia(self):
        pass
    
class podilato(oxima):
    def __init__(self,x,v):
        super().__init__('Ποδήλατο',x,v)

    def xekina(self):
        print('Το ',self.eidos,' ξεκίνησε')

    def stamata(self):
        print('Το ',self.eidos,' σταμάτησε')

    def stripse_aristera(self):
        print('Το ',self.eidos,' έστριψε αριστερά')

    def stripse_dexia(self):
        print('Το ',self.eidos,' έστριψε δεξιά')

class aytokinito(oxima):
    def __init__(self,x,v):
        super().__init__('Αυτοκίνητο',x,v)

    def xekina(self):
        print('Το ',self.eidos,' ξεκίνησε')

    def stamata(self):
        print('Το ',self.eidos,' σταμάτησε')

    def stripse_aristera(self):
        print('Το ',self.eidos,' έστριψε αριστερά')

    def stripse_dexia(self):
        print('Το ',self.eidos,' έστριψε δεξιά') 

# Κυρίως πρόγραμμα
p1=podilato('Κόκκινο',14)
p1.xekina()
p1.stripse_aristera()
p1.stripse_dexia()
p1.stamata()
a1=aytokinito('Μαύρο',1200)
a1.xekina()
a1.stripse_aristera()
a1.stripse_dexia()
a1.stamata()
