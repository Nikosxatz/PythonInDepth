class MyEx1(Exception):
    pass

class MyEx2(Exception):
    pass

class MyEx3(Exception):
    pass

class MyEx4(Exception):
    pass

def f1():
    try:
        f2()
        raise MyEx2
        raise MyEx3
    except MyEx2:
        print('f1 - Επιασα την MyEx2')

def f2():
    try:
        f3()
        raise MyEx4
    except MyEx1:
        print('f2 - Επιασα την MyEx1')
    except MyEx2:
        print('f2 - Επιασα την MyEx2')

def f3():
    try:
        pass
        raise MyEx1
        raise MyEx2
        raise MyEx3
    except MyEx1:
        print('f3 - Επιασα την MyEx1')
 
# Κυρίως πρόγραμμα
try:
    f1()
except MyEx3:
    print('Κ.Π - Επιασα την MyEx3')
except MyEx4:
    print('Κ.Π - Επιασα την MyEx4')
except:
    print('Επιασα κάποια άλλη!!!')
