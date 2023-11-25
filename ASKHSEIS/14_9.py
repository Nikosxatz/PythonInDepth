class arithmos:
    def __init__(self,a):
        self.ar=a
    def __ek(self):
        ekatontades=['','εκατό','διακόσια','τριακόσια','τετρακόσια','πεντακόσια','εξακόσια','επτακόσια','οκτακόσια','εννιακόσια']
        e=self.ar//100
        if e==0:
            return self.__dek()
        else:
            return ekatontades[e]+' '+self.__dek()
    def __dek(self):
        monades=['','ένα','δύο','τρία','τέσσερα','πέντε','έξι','επτά','οκτώ','εννιά','δέκα']
        dekades=['','δέκα','είκοσι','τριάντα','σαράντα','πενήντα','εξήντα','εβδομήντα','ογδόντα','εννενήντα']
        m=self.ar%10
        d=(self.ar%100)//10
        if d==1 and m==1:
            return 'έντεκα'
        elif d==1 and m==2:
            return 'δώδεκα'
        elif d==0:
            return monades[m]
        else:
            return dekades[d]+' '+monades[m]
    def __str__(self):
        if self.ar==0:
            return 'μηδέν'
        else:
            return self.__ek()
    def __lshift__(self,a):
        self.ar=a
    def __invert__(self):
        a = self.ar
        self.ar = int(str(a)[::-1])
# Κυρίως πρόγραμμα    
a1=arithmos(23)
print(str(a1))
a1<<345
print(str(a1))
~a1
print(str(a1))

