class student:
    def __init__(self,o):
        self.onoma=o
        self.bathmoi=[]
        self.cnt=0

    def mo(self):
        s=0
        for b in self.bathmoi:
            s=s+b
        return s/len(self.bathmoi)

    def display(self):
        print('Όνομα ',self.onoma)
        print('Βαθμοί : ',end='')
        for b in self.bathmoi:
            print(b, end=' ')
        print()
        print('Μέσος όρος =','{:4.1f}'.format(self.mo()))
            
    def get_bathmoi(self):
        print('Δώσε βαθμούς για τον ',self.onoma)
        b=float(input('Δώσε βαθμό > '))
        while b>=0:
            self.bathmoi.append(b)
            b=float(input('Δώσε βαθμό > '))
        print('Μπράβο έδωσες ',len(self.bathmoi),'βαθμούς')
        

# Κυρίως πρόγραμμα 
s1=student('Νίκος')    # Δημιουργία αντικειμένου - φοιτητή
s1.get_bathmoi()        
s1.display()
for i in s1:
    print(i)


