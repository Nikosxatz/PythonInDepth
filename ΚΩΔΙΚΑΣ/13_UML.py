class rectangle:
    plithos=0
    def __init__(self,a,b,x):
        self.__plevra_a=a
        self.__plevra_b=b
        self.xroma=x
        rectangle.plithos=rectangle.plithos+1

    def __emvado(self):
        return self.__plevra_a*self.__plevra_b

    def display(self):
        print(self.xroma,' ',self.__plevra_a,'x',self.__plevra_b,' E=',self.__emvado()) 

    def set(self,a,b):
        self.__plevra_a=a
        self.__plevra_b=b

    @classmethod
    def synola(cls):
        print('Σύνολο ορθογωνίων =',cls.plithos)


# Κυρίως πρόγραμμα 
p1=rectangle(10,5,'Πράσινο')    # Δημιουργία πρώτου ορθογωνίου με συγκεκριμένες τιμές
p2=rectangle(7,8,'Κόκκινο')     # Δημιουργία δεύτερου ορθογωνίου με συγκεκριμένες τιμές     
p1.display()                   
p2.display()
p2.set(20,30)
p2.display()
rectangle.synola() 
