class A:
    pl=5
    def __init__(self):
        A.pl=A.pl+1
        
    @classmethod
    def display(cls):
        print(cls.pl)
    
class B(A):
    def __init__(self):
        super().__init__()
            
# Κυρίως πρόγραμμα
obj1=B()
obj2=B()
B.display()




