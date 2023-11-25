def doit(a,b):
    if type(a)==str and type(b)==str:
        return a+b
    elif type(a)==str and type(b)==int:
        return a*b
    elif type(a)==int and type(b)==str:
        return a*b
    else:
        return a-b

    
# Κυρίως πρόγραμμα    
print(doit(3,4.5))
print(doit('Python','3.x'))
print(doit('Python',3))
print(doit(12,'='))
 
