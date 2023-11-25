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

    def __iter__(self):
        self.cnt=0
        return self
            
    def __next__(self):
        self.cnt=self.cnt+1
        if self.cnt>len(self.bathmoi):
            raise StopIteration
        else:
            return self.bathmoi[self.cnt-1]

# Κυρίως πρόγραμμα 
s1=student('Νίκος')    # Δημιουργία αντικειμένου - φοιτητή
s1.get_bathmoi()        
s1.display()
for j in s1:
    print(j)
print('Νέος επαναλήπτης')     
i=iter(s1)
print(next(i))
print(i.__next__())
while True:
    vath=next(i,'##')
    if vath!='##':
        print(vath)
    else:
        break
 


