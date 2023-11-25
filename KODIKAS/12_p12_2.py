import math

class trionymo:
    def __init__(self,s1,s2,s3):
        self.__a=s1
        self.__b=s2
        self.__c=s3
        
    def syntelestes(self,s1,s2,s3):
        self.__a=s1
        self.__b=s2
        self.__c=s3
        
    def __diakrinousa(self):
        d=self.__b**2-4*self.__a*self.__c
        return d

    def exei_pragmatikes_rizes(self):
        if self.__diakrinousa()>=0:
            return True
        else:
            return False

    def rizes(self):
        if self.__diakrinousa()>=0:
            r1=(-self.__b+math.sqrt(self.__diakrinousa()))/(2*self.__a)
            r2=(-self.__b-math.sqrt(self.__diakrinousa()))/(2*self.__a)    
            return (r1,r2)
        else:
            return None

# Κυρίως πρόγραμμα
t1=trionymo(-5,10,-2)
print(t1.rizes())
t1.syntelestes(-2,1,1)
print(t1.rizes())
t1.syntelestes(2,2,2)
print(t1.rizes())

