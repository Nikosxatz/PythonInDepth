def decorator_mesos_str(func):
    def inner(s):
        return func(ord(s[0]),ord(s[1]),ord(s[2]))
    return inner

@decorator_mesos_str
def mesos_oros(a,b,c):
    return (a+b+c)/3

# Κυρίως πρόγραμμα
treis=input('Πληκτρολόγησε 3 χαρακτήρες > ')
mo=mesos_oros(treis)
print('Ο μέσος όρος των κωδικών είναι :',mo)

