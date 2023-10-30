def decorator_mesos_listas_bathmon(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1], val[2]) for val in list_of_tuples]
    return inner

def decorator_megistos_listas_bathmon(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1], val[2]) for val in list_of_tuples]
    return inner

@decorator_mesos_listas_bathmon
def mesos_oros(a, b, c):
    return (a + b + c)/3

@decorator_megistos_listas_bathmon
def megistos(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
# Κυρίως πρόγραμμα
print(mesos_oros([(8, 3, 5.5), (6.5, 7, 9), (10, 5, 3), (6, 7, 8)]))
print(megistos([(8, 3, 5.5), (6.5, 7, 9), (10, 5, 3), (6, 7, 8)]))
