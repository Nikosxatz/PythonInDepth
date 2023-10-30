class rectangle:
    def __init__(self,a,b,x):
        self.__plevra_a=a
        self.__plevra_b=b
        self.xroma=x

    def __emvado(self):
        return self.__plevra_a*self.__plevra_b

    def display(self):
        print(self.xroma,' ',self.__plevra_a,'x',self.__plevra_b,' E=',self.__emvado()) 

    def set(self,a,b=''):
        if type(a) is str:
            self.xroma=a
        elif b=='':
            self.__plevra_a=a
            self.__plevra_b=a
        else:
            self.__plevra_a=a
            self.__plevra_b=b
# Κυρίως πρόγραμμα 
p1=rectangle(10,5,'Πράσινο')    # Δημιουργία ορθογωνίου με συγκεκριμένες τιμές
p1.display()
p1.set('Κόκκινο')
p1.display()
p1.set(7)
p1.display()
p1.set(8,9)
p1.display()
