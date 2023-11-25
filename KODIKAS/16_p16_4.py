class MyEx1(Exception):
    pass

class MyEx2(Exception):
    pass


def f1():
    try:
        f2()
        raise MyEx2
    except MyEx2:
        print('f1 - Έπιασα την MyEx2')
    except MyEx1:
        print('f1 - Έπιασα την MyEx1')

def f2():
    try:
        pass
        raise MyEx1
    except MyEx1:
        print('f2 - Έπιασα την MyEx1')
        raise

# Κυρίως πρόγραμμα
f1()

