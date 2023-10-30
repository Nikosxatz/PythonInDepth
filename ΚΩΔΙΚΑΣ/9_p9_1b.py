import random

def zygoimonoi(Lst):
    zygoi=0
    monoi=0
    for i in Lst:
        if i%2==0:
            zygoi=zygoi+i
        else:
            monoi=monoi+i
    return zygoi,monoi
        
def main():
    a=[]
    for i in range(100):
        a.append(random.randint(1,1000))
    apot=zygoimonoi(a)
    print(apot)
    
# Κυρίως πρόγραμμα
main()
