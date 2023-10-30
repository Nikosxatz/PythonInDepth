class tmima:
  
    def __init__(self,p):
        self.perigrafi=p
        self.foitites=[]
        self.cnt=0

    def display(self):
        print('Τμήμα :',self.perigrafi)
        print('Φοιτητές')
        print('================')
        for f in self.foitites:
            print(f)
        print('================')      
            
    def get_foitites(self):
        print('Δώσε φοιτητές για το τμήμα ',self.perigrafi)
        o=input('Δώσε όνομα ή ENTER για τερματισμό > ')
        while o!='':
            self.foitites.append(o)
            o=input('Δώσε όνομα ή ENTER για τερματισμό > ')
        print('Μπράβο έδωσες ',len(self.foitites),'φοιτητές')

    def __iter__(self):
        self.cnt=0
        return self
            
    def __next__(self):
        self.cnt=self.cnt+1
        if self.cnt>len(self.foitites):
            raise StopIteration
        else:
            return self.foitites[self.cnt-1]

# Κυρίως πρόγραμμα 
t1=tmima('ΤΠΤΕ')    # Δημιουργία αντικειμένου - τμήμα
t1.get_foitites()        
t1.display()
for j in t1:
    print(j)

 


