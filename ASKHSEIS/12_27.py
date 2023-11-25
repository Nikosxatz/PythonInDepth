class year:
    def __init__(self,e):        
        self.etos=e
	
    def disekto(self):
        if (self.etos%4 == 0 and self.etos%100 != 0) or self.etos%400 == 0:
            return True
        else:
            return False

# Κυρίως πρόγραμμα 
while True:
    et=int(input('Δώσε έτος:'))
    if et<0:
        break
    e1=year(et)
    if e1.disekto():
        print('Δίσεκτο')
    else:
        print('Κανονικό')



