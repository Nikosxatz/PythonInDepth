class box:
    def __init__(self,x='Άσπρο',per='-',y=0,p=0,m=0):        
        self.xroma=x
        self.periex=per
        self.__ypsos=y
        self.__platos=p
        self.__mikos=m
        if p==0 and m==0:
            self.__platos=y
            self.__mikos=y   
        
    def info(self):
        print('Χρώμα:',self.xroma) 
        print('Περιεχόμενο:',self.periex) 
        print('Υψος:',self.__ypsos)
        print('Πλάτος:',self.__platos)
        print('Μήκος:',self.__mikos)

    def ogos(self):
        return self.__ypsos*self.__platos*self.__mikos

    def set(self,y,p,m):
        self.__ypsos=y
        self.__platos=p
        self.__mikos=m

    def __del__(self):
        print('Ένα',self.xroma,'κουτί που περιείχε',self.periex,'καταστράφηκε')
        
# Κυρίως πρόγραμμα 
k1=box('Κόκκινο','Τίποτα')
k2=box('Πράσινο','Πατάτες',10,20,30)
size=int(input('Δώσε τιμή:'))
k3=box('Κίτρινο','Αυγά',size)
print('Ογκος=',k2.ogos())
k1.set(7,8,9)
k1.info()
k2.info()
k3.info()
k2=k1
