class biblio:
    def __init__(self,t='',s=0,p=0):        
        self.titlos=t
        self.selides=s
        self.__timi=p
        
    def info(self):
        print('Τίτλος:',self.titlos) 
        print('Σελίδες:',self.selides) 
        print('Τιμή:',self.__timi)
	
    def set_timi(self,p):
        self.__timi=p
        
# Κυρίως πρόγραμμα 
b1=biblio('Η γλώσσα Python σε βάθος',700,50)
b2=biblio('Η γλώσσα C σε βάθος',800,65)
b3=biblio('Η γλώσσα C++ σε βάθος',900,80)
b1.info()
b2.info()
b3.info()
